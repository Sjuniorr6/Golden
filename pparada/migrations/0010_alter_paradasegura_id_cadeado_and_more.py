# Generated by Django 5.1.1 on 2024-10-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pparada', '0009_alter_paradasegura_descreva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paradasegura',
            name='id_cadeado',
            field=models.CharField(blank=True, choices=[('POSTO DA SERRA', [('1017242', '1017242'), ('1017287', '1017287'), ('1016690', '1016690'), ('1017601', '1017601'), ('1017716', '1017716')]), ('POSTO BURITIZINHO', [('1017692', '1017692'), ('1017132', '1017132'), ('1018072', '1018072'), ('1016895', '1016895'), ('1017935', '1017935')]), ('POSTO BRASILEIRÃO', [('1017977', '1017977'), ('1018035', '1018035'), ('1017246', '1017246'), ('1017972', '1017972'), ('1017819', '1017819')]), ('POSTO TREVÃO', [('1016679', '1016679'), ('1017927', '1017927'), ('1017961', '1017961'), ('1017614', '1017614'), ('1018144', '1018144')]), ('POSTO JN', [('1017994', '1017994'), ('1017702', '1017702'), ('1017274', '1017274'), ('1018134', '1018134'), ('1017649', '1017649')]), ('POSTO CAPIXABOM', [('1018057', '1018057'), ('1017084', '1017084'), ('1017685', '1017685'), ('1017695', '1017695'), ('1017971', '1017971')]), ('POSTO GRAAL RUBI', [('1017812', '1017812'), ('1017967', '1017967'), ('1017759', '1017759'), ('1017214', '1017214'), ('1017663', '1017663')])], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paradasegura',
            name='id_rastreador',
            field=models.CharField(blank=True, choices=[('POSTO DA SERRA', [('807613081', '807613081'), ('807612797', '807612797'), ('807612814', '807612814'), ('807548077', '807548077'), ('807587224', '807587224')]), ('POSTO BURITIZINHO', [('807612587', '807612587'), ('807587474', '807587474'), ('807612614', '807612614'), ('807612614', '807612614'), ('807587471', '807587471')]), ('POSTO BRASILEIRÃO', [('807612727', '807612727'), ('807558802', '807558802'), ('807612819', '807612819'), ('807558824', '807558824'), ('807613823', '807613823')]), ('POSTO TREVÃO', [('807612611', '807612611'), ('807587594', '807587594'), ('807612586', '807612586'), ('807587570', '807587570'), ('807612716', '807612716')]), ('POSTO JN', [('807558949', '807558949'), ('807296832', '807296832'), ('807612622', '807612622'), ('807613796', '807613796'), ('807296849', '807296849')]), ('POSTO CAPIXABOM', [('807587475', '807587475'), ('807612823', '807612823'), ('807578510', '807578510'), ('807612584', '807612584'), ('807613790', '807613790')]), ('POSTO GRAAL RUBI', [('807613824', '807613824'), ('807558953', '807558953'), ('807296838', '807296838'), ('807612713', '807612713'), ('807612701', '807612701')])], max_length=255, null=True),
        ),
    ]