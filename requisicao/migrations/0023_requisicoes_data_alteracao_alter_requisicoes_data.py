# Generated by Django 5.1.1 on 2024-10-10 14:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0022_alter_requisicoes_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisicoes',
            name='data_alteracao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='requisicoes',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
