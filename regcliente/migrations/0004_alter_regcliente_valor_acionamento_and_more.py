# Generated by Django 5.1.1 on 2024-09-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regcliente', '0003_alter_regcliente_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regcliente',
            name='valor_acionamento',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='regcliente',
            name='valor_exedente',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='regcliente',
            name='valorkm',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=10, null=True),
        ),
    ]

