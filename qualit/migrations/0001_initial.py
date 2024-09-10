# Generated by Django 5.0.7 on 2024-09-04 14:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acompanhamento', '0012_rename_quabtidade_clientes_quantidade'),
        ('produto', '0004_produto_marca_produto_quantidade_alter_produto_preco'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('numero_requisicao', models.CharField(max_length=50)),
                ('tipo_pedido', models.CharField(blank=True, choices=[('Tipo de Faturamento', 'Tipo de Faturamento'), ('Aquisicão Nova', 'Aquisicão Nova'), ('Manutenção', 'Manutenção'), ('Aditivo', 'Aditivo'), ('Acessorios', 'Acessorios'), ('Extravio', 'Extravio'), ('Texte', 'Texte'), ('Isca Fast', 'Isca Fast'), ('Isca Fast Agente', 'Isca Fast Agente'), ('Antenista', 'Antenista'), ('Reversa', 'Reversa')], max_length=100, null=True)),
                ('comercial', models.CharField(max_length=100)),
                ('imei', models.CharField(max_length=50)),
                ('id_equipamento', models.CharField(max_length=50)),
                ('device_id', models.CharField(max_length=50)),
                ('iccid_novo', models.CharField(max_length=50)),
                ('contrato', models.CharField(blank=True, choices=[('', ''), ('Descartavel', 'Descartavel'), ('Retornavel', 'Retornavel')], max_length=50, null=True)),
                ('tp', models.CharField(blank=True, choices=[('5', '5'), ('10', '10'), ('15', '15'), ('30', '30'), ('60', '60'), ('360', '360'), ('720', '720')], max_length=50, null=True)),
                ('operadora', models.CharField(choices=[('ESEYE', 'ESEYE'), ('1NCE', '1NCE')], max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualit_nome', to='acompanhamento.clientes')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualit_produto', to='produto.produto')),
                ('usuario', models.ForeignKey(default=10000000000, on_delete=django.db.models.deletion.CASCADE, related_name='qualit_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
