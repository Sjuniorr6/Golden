# Generated by Django 5.0.7 on 2024-08-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acompanhamento', '0003_alter_cliente_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]