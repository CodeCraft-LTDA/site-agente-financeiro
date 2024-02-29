from django.contrib import admin
from .models import TipoSelecao, Acao, PDFFile

# Register your models here.
admin.site.register(TipoSelecao)
admin.site.register(Acao)
admin.site.register(PDFFile)