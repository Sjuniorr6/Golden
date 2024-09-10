# Generated by Django 5.0.7 on 2024-08-08 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acompanhamento', '0006_cliente_telefone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='telefone',
        ),
        migrations.AddField(
            model_name='cliente',
            name='inicio_de_contrato',
            field=models.CharField(default=1, max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='vigencia',
            field=models.CharField(default=2, max_length=14),
            preserve_default=False,
        ),
    ]