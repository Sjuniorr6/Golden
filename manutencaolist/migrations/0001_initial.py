# Generated by Django 5.0.7 on 2024-09-12 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acompanhamento', '0001_initial'),
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='manutensaolis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_entrada', models.CharField(blank=True, choices=[('Manutenção', 'Manutenção'), ('Devolução/Estoque', 'Devolução/Estoque')], max_length=50, null=True)),
                ('motivo', models.CharField(blank=True, choices=[('', ''), ('Manutenção', 'Manutenção'), ('Devolução/Estoque', 'Devolução/Estoque')], max_length=50, null=True)),
                ('tipo_customizacao', models.CharField(blank=True, choices=[('Sem customização', 'Sem customização'), ('Caixa de papelão', 'Caixa de papelão'), ('Caixa de papelão (bateria desacoplada)', 'Caixa de papelão (bateria desacoplada)')], max_length=50, null=True)),
                ('recebimento', models.CharField(blank=True, choices=[('Correios/Transportadora', 'Correios/Transportadora'), ('Entrega na base', 'Entrega na base'), ('Retirado pelo cliente', 'Retirado pelo cliente')], max_length=50, null=True)),
                ('entregue_por_retirado_por', models.CharField(default='', max_length=100)),
                ('id_equipamentos', models.CharField(blank=True, default='', max_length=100)),
                ('faturamento', models.CharField(blank=True, choices=[('Com_Custo', 'Com Custo'), ('Sem_Custo', 'Sem Custo')], max_length=50, null=True)),
                ('tipo_problema', models.CharField(blank=True, choices=[('Oxidação', 'Oxidação'), ('Placa Danificada', 'Placa Danificada'), ('Placa danificada SEM CUSTO', 'Placa danificada SEM CUSTO'), ('USB Danificado', 'USB Danificado'), ('USB Danificado SEM CUSTO', 'USB Danificado SEM CUSTO'), ('Botão de acionamento Danificado', 'Botão de acionamento Danificado'), ('Botão de acionamento Danificado SEM CUSTO', 'Botão de acionamento Danificado SEM CUSTO'), ('Antena LoRa Danificada', 'Antena LoRa Danificada'), ('Sem problemas Identificados', 'Sem problemas Identificados')], max_length=50, null=True)),
                ('customizacao', models.TextField(blank=True, default='', max_length=250)),
                ('numero_equipamento', models.TextField(blank=True, default='', max_length=250)),
                ('tratativa', models.CharField(blank=True, choices=[('Oxidação', 'Oxidação'), ('Placa Danificada', 'Placa Danificada'), ('USB Danificado', 'USB Danificado'), ('Botão de acionamento Danificado', 'Botão de acionamento Danificado'), ('Antena LoRa Danificada', 'Antena LoRa Danificada'), ('USB Sem problemas Identificados', 'USB Sem problemas Identificados')], max_length=50, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/')),
                ('status', models.CharField(blank=True, choices=[('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado'), ('Pendente', 'Pendente')], default='Pendente', max_length=50, null=True)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registromanutencao_nome', to='acompanhamento.clientes')),
                ('tipo_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registromanutencao_produto', to='produto.produto')),
            ],
        ),
    ]
