# Generated by Django 5.1.1 on 2024-09-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t42', '0012_alter_t42model_estoque_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t42model',
            name='estoque_status',
            field=models.CharField(blank=True, choices=[('Estoque', 'Estoque'), ('Retornando', 'Retornando'), ('Enviado', 'Enviado'), ('Extraviado', 'Extraviado')], max_length=50, null=True),
        ),
    ]