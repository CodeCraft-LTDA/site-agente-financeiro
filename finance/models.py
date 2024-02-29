from django.db import models
from django.contrib.auth.models import User

class TipoSelecao(models.Model):
    nome = models.CharField(max_length=100)

class PDFFile(models.Model):
    upload_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='pdfs/')
    
    class Meta:
        ordering = ['-upload_date']
        
class AcessoPDF(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_acesso = models.DateField()
    pdf_file = models.ForeignKey(PDFFile, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('usuario', 'data_acesso', 'pdf_file')

class Acao(models.Model):
    DIRECAO_CHOICES = [
        ('subindo', 'Subir'),
        ('descendo', 'Descer'),
        ('manter', 'Manter'),
    ]
    SENTIMENTO_CHOICES = [
        ('positivo', 'Positivo'),
        ('negativo', 'Negativo'),
        ('cauteloso', 'Cauteloso'),
    ]
    METRICA_CHOICES = [
        ('compra', 'Comprar'),
        ('venda', 'Vender'),
        ('manter', 'Manter'),
    ]
    DECISAO_CHOICES = [
        ('compra', 'Comprar'),
        ('venda', 'Vender'),
        ('manter', 'Manter'),
    ]
    nome = models.CharField(max_length=100)
    tipo_selecao = models.ForeignKey(TipoSelecao, on_delete=models.CASCADE)
    metrica = models.CharField(max_length=9, choices=METRICA_CHOICES)
    direcao = models.CharField(max_length=8, choices=DIRECAO_CHOICES)  # Adjusted max_length to 8
    sentimento = models.CharField(max_length=9, choices=SENTIMENTO_CHOICES)  # Adjusted max_length to 9
    decisao = models.CharField(max_length=9, choices=DECISAO_CHOICES)
