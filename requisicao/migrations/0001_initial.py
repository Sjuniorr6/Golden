# Generated by Django 5.1.1 on 2024-10-02 12:34

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
            name='estoque_antenista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('ALCIDES', 'ALCIDES'), ('EZEQUIEL', 'EZEQUIEL'), ('NILDO', 'NILDO'), ('ALEX', 'ALEX'), ('ANDERSON', 'ANDERSON'), ('ANTONIEQUE', 'ANTONIEQUE'), ('OSNI', 'OSNI'), ('ELTON', 'ELTON'), ('NEY', 'NEY'), ('ANDRÉ', 'ANDRÉ'), ('RILDO', 'RILDO'), ('WELLINGTHON', 'WELLINGTHON'), ('GERSON WALACE', 'GERSON WALACE'), ('JUSTINO', 'JUSTINO'), ('ANTONIO', 'ANTONIO'), ('FRANCISCO', 'FRANCISCO'), ('OSMAN', 'OSMAN'), ('TONHARA', 'TONHARA'), ('EMERSON', 'EMERSON'), ('MARCELO', 'MARCELO'), ('JEFFERSON', 'JEFFERSON'), ('GUILHERME', 'GUILHERME'), ('MARCIO', 'MARCIO'), ('SAMPAIO', 'SAMPAIO'), ('DIOGO', 'DIOGO'), ('WESLEY', 'WESLEY'), ('EVERALDO / SAMUEL', 'EVERALDO / SAMUEL'), ('ERIK', 'ERIK'), ('LUCAS CARVALHO', 'LUCAS CARVALHO'), ('RODRIGO', 'RODRIGO'), ('PITTA', 'PITTA'), ('JUSTO', 'JUSTO'), ('PAULO HENRIQUE', 'PAULO HENRIQUE'), ('EDUARDO', 'EDUARDO'), ('YURI', 'YURI'), ('RAFAEL', 'RAFAEL')], max_length=50)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('tipo_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='antenista_produto', to='produto.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Requisicoes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('contrato', models.CharField(blank=True, choices=[('', ''), ('Descartavel', 'Descartavel'), ('Retornavel', 'Retornavel')], max_length=50, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=25, null=True)),
                ('numero_de_equipamentos', models.CharField(blank=True, max_length=14, null=True)),
                ('inicio_de_contrato', models.DateField(blank=True, null=True)),
                ('vigencia', models.CharField(blank=True, choices=[('N/A', 'N/A'), ('6', '6'), ('12', '12'), ('18', '18'), ('24', '24'), ('30', '30'), ('36', '36'), ('48', '48')], max_length=50, null=True)),
                ('customizacao', models.CharField(blank=True, choices=[('N/A', 'N/A'), ('6', '6'), ('12', '12'), ('18', '18'), ('24', '24'), ('30', '30'), ('36', '36'), ('48', '48')], max_length=50, null=True)),
                ('data', models.DateField(auto_now=True)),
                ('tipo_customizacao', models.CharField(blank=True, choices=[('Sem custumização', 'Sem custumização'), ('Caixa de papelão', 'Caixa de papelão'), ('Caixa de papelão (bateria desacoplada)', 'Caixa de papelão (bateria desacoplada)'), ('Caixa de papelão + DF', 'Caixa de papelão + DF'), ('Termo branco', 'Termo branco'), ('Termo branco + D.F ', 'Termo branco + D.F'), ('Termo branco slim ', 'Termo branco slim'), ('Termo branco slim + D.F +EQT  ', 'Termo branco slim + D.F +EQT'), ('Termo cinza slim + D.F +EQT  ', 'Termo cinza slim + D.F +EQT'), ('Termo branco  (isopor) ', 'Termo branco  (isopor)'), ('Termo branco - bateria externa ', 'Termo branco - bateria externa'), ('Termo marrom + imã', 'Termo marrom + imã'), ('Termo cinza', 'Termo cinza'), ('Termo cinza + imã', 'Termo cinza + imã'), ('Termo preto', 'Termo preto'), ('Termo preto + imã', 'Termo preto + imã'), ('Termo brabco |marrim-slim', 'Termo brabco |marrim-slim'), ('Termo marrom slim +D.F + EQT', 'Termo marrom slim +D.F + EQT'), ('Termo marrom', 'Termo marrom'), ('Caixa blindada', 'Caixa blindada'), ('Tênis/ Sapato', 'Tênis/ Sapato'), ('Projetor', 'Projetor'), ('Caixa de som', 'Caixa de som'), ('Luminaria', 'Luminaria'), ('Alexa', 'Alexa'), ('Video Game', 'Video Game'), ('Secador de cabelo', 'Secador de cabelo'), ('Roteador', 'Roteador'), ('Relogio digital', 'Relogio digital')], max_length=50, null=True)),
                ('antenista', models.CharField(blank=True, max_length=50, null=True)),
                ('envio', models.CharField(blank=True, choices=[('Agente', 'Agente'), ('Retirada na base', 'Retirada na base'), ('Motoboy', 'Motoboy'), ('transportadora', 'Transportadora'), ('Correio', 'Correio'), ('Comercial', 'Comercial')], max_length=50, null=True)),
                ('taxa_envio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('comercial', models.CharField(blank=True, default='', max_length=100)),
                ('carregador', models.CharField(blank=True, default='', max_length=100)),
                ('motivo', models.CharField(blank=True, choices=[('Tipo de Faturamento', 'Tipo de Faturamento'), ('Aquisicão Nova', 'Aquisicão Nova'), ('Manutenção', 'Manutenção'), ('Aditivo', 'Aditivo'), ('Acessórios', 'Acessórios'), ('Extravio', 'Extravio'), ('Teste', 'Teste'), ('Isca Fast', 'Isca Fast'), ('Isca Fast - Agente', 'Isca Fast - Agente'), ('Antenista', 'Antenista'), ('Reversa', 'Reversa'), ('Isca FAST', 'Isca FAST'), ('Estoque Antenista', 'Estoque Antenista')], default='', max_length=50, null=True)),
                ('cabo', models.CharField(blank=True, default='', max_length=100)),
                ('tipo_fatura', models.CharField(blank=True, choices=[('Com Custo', 'Com Custo'), ('Sem Custo', 'Sem Custo')], max_length=50, null=True)),
                ('valor_unitario', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('valor_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('forma_pagamento', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('observacoes', models.TextField(blank=True, default='', max_length=250, null=True)),
                ('status', models.CharField(blank=True, default='Pendente', max_length=50, null=True)),
                ('TP', models.CharField(blank=True, choices=[('5', '5'), ('10', '10'), ('15', '15'), ('30', '30'), ('60', '60'), ('360', '360'), ('720', '720')], max_length=50, null=True)),
                ('status_faturamento', models.CharField(blank=True, choices=[('', ''), ('A Faturar', 'A Faturar'), ('Faturado sem taxa', 'Faturado sem taxa'), ('Faturado com taxa', 'Faturado com taxa'), ('Pendente', 'Pendente'), ('Pendente sem Contrato', 'Pendente sem Contrato'), ('Pendente Sem Termo', 'Pendente Sem Termo'), ('Pendente Sem Contrato', 'Pendente Sem Contrato'), ('Sem Custo', 'Sem Custo'), ('Dados invalidos', 'Dados invalidos')], default='', max_length=50, null=True)),
                ('id_equipamentos', models.TextField(blank=True, default='', max_length=1200, null=True)),
                ('faturamento', models.CharField(blank=True, choices=[('', ''), ('A Faturar', 'A Faturar'), ('Faturado sem taxa', 'Faturado sem taxa'), ('Faturado com taxa', 'Faturado com taxa'), ('Pendente', 'Pendente'), ('Pendente sem Contrato', 'Pendente sem Contrato'), ('Pendente Sem Termo', 'Pendente Sem Termo'), ('Pendente Sem Contrato', 'Pendente Sem Contrato'), ('Sem Custo', 'Sem Custo'), ('Dados invalidos', 'Dados invalidos')], default='', max_length=1200)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisicoes_nome', to='acompanhamento.clientes')),
                ('tipo_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisicoes_produto', to='produto.produto')),
            ],
        ),
    ]
