# Generated by Django 5.0.7 on 2024-09-19 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t42', '0014_alter_t42model_estoque_status_alter_t42model_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t42model',
            name='estoque_status',
            field=models.CharField(blank=True, choices=[('Estoque', 'Estoque'), ('Retornando', 'Retornando'), ('Enviado', 'Enviado'), ('Estraviado', 'Estraviado')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='t42model',
            name='status',
            field=models.CharField(blank=True, choices=[('', ''), ('Atualizado e Configurado', 'Atualizado e Configurado'), ('Não Atualizado', 'Não Atualizado'), ('Não Configurado', 'Não Configurado'), ('Manutenção', 'Manutenção')], max_length=50, null=True),
        ),
    ]