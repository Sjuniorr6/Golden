# Generated by Django 5.1.1 on 2024-09-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t42', '0004_t42model_reversa'),
    ]

    operations = [
        migrations.AddField(
            model_name='t42model',
            name='estoque_status',
            field=models.CharField(blank=True, choices=[('estoque', 'Estoque'), ('retornado', 'Retornado'), ('enviado', 'Enviado'), ('extraviado', 'Extraviado')], max_length=50, null=True),
        ),
    ]