from django.contrib import admin
from .models import TipoSelecao, Acao, PDFFile, AcessoPDF

# Register your models here.
admin.site.register(TipoSelecao)
admin.site.register(Acao)
admin.site.register(PDFFile)
admin.site.register(AcessoPDF)