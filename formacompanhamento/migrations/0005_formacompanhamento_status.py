# Generated by Django 5.1.1 on 2024-09-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacompanhamento', '0004_alter_formacompanhamento_agente'),
    ]

    operations = [
        migrations.AddField(
            model_name='formacompanhamento',
            name='status',
            field=models.CharField(blank=True, default='Pendente', max_length=10, null=True),
        ),
    ]