# Generated by Django 4.2.10 on 2024-02-27 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSelecao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('metrica', models.CharField(choices=[('compra', 'Comprar'), ('venda', 'Vender'), ('manter', 'Manter')], max_length=9)),
                ('direcao', models.CharField(choices=[('subindo', 'Subir'), ('descendo', 'Descer'), ('manter', 'Manter')], max_length=8)),
                ('sentimento', models.CharField(choices=[('positivo', 'Positivo'), ('negativo', 'Negativo'), ('cauteloso', 'Cauteloso')], max_length=9)),
                ('decisao', models.CharField(choices=[('compra', 'Comprar'), ('venda', 'Vender'), ('manter', 'Manter')], max_length=9)),
                ('tipo_selecao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.tiposelecao')),
            ],
        ),
    ]
