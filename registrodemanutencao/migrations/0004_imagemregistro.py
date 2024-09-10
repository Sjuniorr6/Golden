# Generated by Django 5.0.7 on 2024-08-26 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrodemanutencao', '0003_registrodemanutencao_arquivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagemRegistro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagens_registros/')),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='registrodemanutencao.registrodemanutencao')),
            ],
        ),
    ]
