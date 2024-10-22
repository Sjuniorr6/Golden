# Generated by Django 5.1.1 on 2024-10-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0006_rename_horario_saida_paradasegura_horario_de_saida_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paradasegura',
            name='descreva',
            field=models.CharField(blank=True, choices=[('POSTO DA SERRA', 'POSTO DA SERRA'), ('POSTO BURITIZINHO', 'POSTO BURITIZINHO'), ('POSTO BRASILEIRÃO', 'POSTO BRASILEIRÃO'), ('POSTO TREVÃO', 'POSTO TREVÃO'), ('POSTO JN', 'POSTO JN'), ('POSTO CAPIXABOM', 'POSTO CAPIXABOM'), ('POSTO GRAAL RUBI', 'POSTO GRAAL RUBI')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paradasegura',
            name='tipo_posto',
            field=models.CharField(blank=True, choices=[('POSTO DA SERRA', 'POSTO DA SERRA'), ('POSTO BURITIZINHO', 'POSTO BURITIZINHO'), ('POSTO BRASILEIRÃO', 'POSTO BRASILEIRÃO'), ('POSTO TREVÃO', 'POSTO TREVÃO'), ('POSTO JN', 'POSTO JN'), ('POSTO CAPIXABOM', 'POSTO CAPIXABOM'), ('POSTO GRAAL RUBI', 'POSTO GRAAL RUBI')], default='Pendente', max_length=255, null=True),
        ),
    ]