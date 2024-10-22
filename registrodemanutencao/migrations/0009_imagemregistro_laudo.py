# Generated by Django 5.1.1 on 2024-10-15 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrodemanutencao', '0008_criarlaudo_id_manutenção'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemregistro',
            name='laudo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='registrodemanutencao.criarlaudo'),
        ),
    ]