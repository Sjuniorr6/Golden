# Generated by Django 5.0.7 on 2024-08-12 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acompanhamento', '0008_alter_cliente_inicio_de_contrato'),
        ('requisicao', '0002_alter_requisicoes_nome_delete_cliente'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Clientes',
        ),
    ]
