# Generated by Django 5.0.7 on 2024-09-23 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acompanhamento', '0005_alter_clientes_cnpj'),
        ('produto', '0003_remove_produto_descricao_remove_produto_preco_and_more'),
        ('requisicao', '0004_alter_requisicoes_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicoes',
            name='motivo',
            field=models.CharField(blank=True, choices=[('Tipo de Faturamento', 'Tipo de Faturamento'), ('Aquisicão Nova', 'Aquisicão Nova'), ('Manutenção', 'Manutenção'), ('Aditivo', 'Aditivo'), ('Acessorios', 'Acessorios'), ('Extravio', 'Extravio'), ('Texte', 'Texte'), ('Isca Fast', 'Isca Fast'), ('Isca Fast Agente', 'Isca Fast Agente'), ('Antenista', 'Antenista'), ('Reversa', 'Reversa'), ('Isca FAST', 'Isca FAST'), ('Estoque Antenista', 'Estoque Antenista')], default='', max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='estoque_antenista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='antenista_nome', to='acompanhamento.clientes')),
                ('tipo_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='antenista_produto', to='produto.produto')),
            ],
        ),
    ]