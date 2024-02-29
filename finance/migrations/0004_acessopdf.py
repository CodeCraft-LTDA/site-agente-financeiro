# Generated by Django 4.2.10 on 2024-02-29 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0003_alter_pdffile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcessoPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_acesso', models.DateField()),
                ('pdf_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.pdffile')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario', 'data_acesso', 'pdf_file')},
            },
        ),
    ]
