# Generated by Django 5.0.7 on 2024-08-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={},
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='create',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefone',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(max_length=255),
        ),
    ]