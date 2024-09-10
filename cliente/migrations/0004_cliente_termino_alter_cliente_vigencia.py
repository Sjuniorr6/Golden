# Generated by Django 5.0.7 on 2024-08-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_cliente_inicio_de_contrato_cliente_vigencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='termino',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='vigencia',
            field=models.CharField(blank=True, choices=[('', ''), ('12', '12'), ('24', '24'), ('36', '36'), ('48', '48')], max_length=50, null=True),
        ),
    ]
