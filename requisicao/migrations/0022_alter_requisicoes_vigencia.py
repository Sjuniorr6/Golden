# Generated by Django 5.0.7 on 2024-09-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0021_requisicoes_id_equipamentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicoes',
            name='vigencia',
            field=models.CharField(blank=True, choices=[('6', '6'), ('12', '12'), ('18', '18'), ('24', '24'), ('36', '36')], default='', max_length=50, null=True),
        ),
    ]
