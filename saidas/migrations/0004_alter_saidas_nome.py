# Generated by Django 5.0.7 on 2024-08-20 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_produto_marca_produto_quantidade_alter_produto_preco'),
        ('saidas', '0003_saidas_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saidas',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saida_produto', to='produto.produto'),
        ),
    ]