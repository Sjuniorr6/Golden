# Generated by Django 5.1.1 on 2024-09-18 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_remove_produto_marca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='preco',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='quantidade',
        ),
    ]