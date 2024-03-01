from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Acao, PDFFile, AcessoPDF
from django.views import View
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import PermissionDenied
import datetime

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def price(request):
    return render(request, 'price.html')

def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login/')
def definition(request):
    return render(request, 'definition.html')

def change_password(request):
    return render(request, 'change_password.html')

@login_required(login_url='login/')
def finance(request):
    acoes = Acao.objects.all()
    return render(request, 'finance.html', {'acoes': acoes})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Use o alias aqui
            return redirect('index')  # Ou a URL de redirecionamento desejada
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form_usuario': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Garante que este é o lugar correto da chamada
                return redirect('finance')
            else:
                messages.error(request, "Username ou password inválidos.")
        else:
            messages.error(request, "Username ou password inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/login')
def pdf_by_date(request, year, month, day):
    data_especificada = datetime.date(year, month, day)
    hoje = datetime.date.today()
    
    # Verificação inicial para acesso não autorizado
    if not request.session.get('redirected_to_today_pdf', False):
        return HttpResponse("Acesso não autorizado.", status=403)

    if data_especificada != hoje:
        return HttpResponse("Acesso apenas para o dia corrente.", status=403)

    # Verifica se já existe um acesso registrado para hoje
    if AcessoPDF.objects.filter(usuario=request.user, data_acesso=hoje).exists():
        return HttpResponse("Acesso ao PDF já realizado hoje.", status=403)

    try:
        pdf_file = PDFFile.objects.get(upload_date=data_especificada)
    except PDFFile.DoesNotExist:
        return HttpResponse("PDF não encontrado para a data especificada.", status=403)
    
    # Registra o acesso antes de fornecer o arquivo, agora garantindo que isso ocorra na sequência correta
    AcessoPDF.objects.create(usuario=request.user, data_acesso=hoje, pdf_file=pdf_file)
    
    # Remove a flag da sessão após todas as verificações terem passado
    request.session.pop('redirected_to_today_pdf', None)

    file_path = pdf_file.file.path
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{pdf_file.file.name}"'
        return response
    
def redirect_to_today_pdf(request):
    today = datetime.date.today()
    request.session['redirected_to_today_pdf'] = True
    return HttpResponseRedirect(reverse('pdf_by_date', args=(today.year, today.month, today.day)))