# Generated by Django 5.0.7 on 2024-08-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acompanhamento', '0002_cliente_delete_exemplomodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
