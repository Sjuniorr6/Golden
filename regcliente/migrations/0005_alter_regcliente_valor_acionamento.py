# Generated by Django 5.1.1 on 2024-09-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regcliente', '0004_alter_regcliente_valor_acionamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regcliente',
            name='valor_acionamento',
            field=models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=10, null=True),
        ),
    ]