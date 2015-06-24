# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CirculatingPumpLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('CPID', models.SmallIntegerField(default=1, choices=[(1, b'1'), (2, b'2')])),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
        migrations.CreateModel(
            name='CPFlowmeterLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('temperature', models.FloatField()),
                ('currentFlux', models.SmallIntegerField()),
                ('integralFlux', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DeepwellPump1Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('waterLevel', models.CharField(default=b'', max_length=2, choices=[(b'AP', b'\xec\xa0\x81\xec\xa0\x95'), (b'NA', b'\xeb\xb6\x80\xec\xa0\x81\xec\xa0\x95')])),
            ],
        ),
        migrations.CreateModel(
            name='DeepwellPump2Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('waterLevel', models.CharField(default=b'', max_length=2, choices=[(b'AP', b'\xec\xa0\x81\xec\xa0\x95'), (b'NA', b'\xeb\xb6\x80\xec\xa0\x81\xec\xa0\x95')])),
            ],
        ),
        migrations.CreateModel(
            name='DeepwellPump3Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('waterLevel', models.CharField(default=b'', max_length=2, choices=[(b'AP', b'\xec\xa0\x81\xec\xa0\x95'), (b'NA', b'\xeb\xb6\x80\xec\xa0\x81\xec\xa0\x95')])),
            ],
        ),
        migrations.CreateModel(
            name='DeepwellPump4Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('waterLevel', models.CharField(default=b'', max_length=2, choices=[(b'AP', b'\xec\xa0\x81\xec\xa0\x95'), (b'NA', b'\xeb\xb6\x80\xec\xa0\x81\xec\xa0\x95')])),
            ],
        ),
        migrations.CreateModel(
            name='DWPFlowmeterLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('temperature', models.FloatField()),
                ('currentFlux', models.SmallIntegerField()),
                ('integralFlux', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HeatPump1Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
        migrations.CreateModel(
            name='HeatPump2Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
        migrations.CreateModel(
            name='HeatPump3Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
        migrations.CreateModel(
            name='HeatPump4Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
        migrations.CreateModel(
            name='HeatPump5Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
        migrations.CreateModel(
            name='HeatPump6Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
        migrations.CreateModel(
            name='InverterLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('inverterID', models.SmallIntegerField(default=1, choices=[(1, b'Inverter1'), (2, b'Inverter2')])),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('switch', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('RPM', models.SmallIntegerField()),
                ('Hz', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperationLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('opMode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'\xec\x88\x98\xeb\x8f\x99'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')])),
                ('tempMode', models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9')])),
                ('HP1', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('HP2', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('HP3', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('HP4', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('HP5', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('HP6', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('DWP1', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('DWP2', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('DWP3', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('DWP4', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('CP1', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('CP2', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
                ('Inverter', models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
        migrations.CreateModel(
            name='OperationSwitchControl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('location', models.CharField(max_length=4, choices=[(b'HP1', b'\xed\x9e\x88\xed\x8a\xb8 \xed\x8e\x8c\xed\x94\x84 1'), (b'HP2', b'\xed\x9e\x88\xed\x8a\xb8 \xed\x8e\x8c\xed\x94\x84 2'), (b'HP3', b'\xed\x9e\x88\xed\x8a\xb8 \xed\x8e\x8c\xed\x94\x84 3'), (b'HP4', b'\xed\x9e\x88\xed\x8a\xb8 \xed\x8e\x8c\xed\x94\x84 4'), (b'HP5', b'\xed\x9e\x88\xed\x8a\xb8 \xed\x8e\x8c\xed\x94\x84 5'), (b'HP6', b'\xed\x9e\x88\xed\x8a\xb8 \xed\x8e\x8c\xed\x94\x84 6'), (b'DWP1', b'\xec\x8b\xac\xec\xa0\x95 \xed\x8e\x8c\xed\x94\x84 1'), (b'DWP2', b'\xec\x8b\xac\xec\xa0\x95 \xed\x8e\x8c\xed\x94\x84 2'), (b'DWP3', b'\xec\x8b\xac\xec\xa0\x95 \xed\x8e\x8c\xed\x94\x84 3'), (b'DWP4', b'\xec\x8b\xac\xec\xa0\x95 \xed\x8e\x8c\xed\x94\x84 4'), (b'CP1', b'\xec\x88\x9c\xed\x99\x98 \xed\x8e\x8c\xed\x94\x84 1'), (b'CP2', b'\xec\x88\x9c\xed\x99\x98 \xed\x8e\x8c\xed\x94\x84 2'), (b'IV', b'\xec\x9d\xb8\xeb\xb2\x84\xed\x84\xb0')])),
                ('switch', models.CharField(max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
        migrations.CreateModel(
            name='PowerConsumptionLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('currentPowerConsumption', models.IntegerField()),
                ('integralPowerConsumption', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RefrigerationTonLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
                ('RT', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TempHEIn1Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHEIn2Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHEOut1Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHEOut2Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPIn1Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPIn2Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPIn3Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPIn4Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPIn5Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPIn6Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPOut1Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPOut2Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPOut3Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPOut4Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPOut5Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TempHPOut6Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TubeWellLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('T1level', models.FloatField()),
                ('T1temp', models.FloatField()),
                ('T2level', models.FloatField()),
                ('T2temp', models.FloatField()),
                ('T3level', models.FloatField()),
                ('T3temp', models.FloatField()),
                ('T4level', models.FloatField()),
                ('T4temp', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HEI1',
            field=models.ForeignKey(to='monitor.TempHEIn1Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HEI2',
            field=models.ForeignKey(to='monitor.TempHEIn2Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HEO1',
            field=models.ForeignKey(to='monitor.TempHEOut1Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HEO2',
            field=models.ForeignKey(to='monitor.TempHEOut2Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPI1',
            field=models.ForeignKey(to='monitor.TempHPIn1Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPI2',
            field=models.ForeignKey(to='monitor.TempHPIn2Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPI3',
            field=models.ForeignKey(to='monitor.TempHPIn3Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPI4',
            field=models.ForeignKey(to='monitor.TempHPIn4Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPI5',
            field=models.ForeignKey(to='monitor.TempHPIn5Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPI6',
            field=models.ForeignKey(to='monitor.TempHPIn6Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPO1',
            field=models.ForeignKey(to='monitor.TempHPOut1Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPO2',
            field=models.ForeignKey(to='monitor.TempHPOut2Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPO3',
            field=models.ForeignKey(to='monitor.TempHPOut3Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPO4',
            field=models.ForeignKey(to='monitor.TempHPOut4Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPO5',
            field=models.ForeignKey(to='monitor.TempHPOut5Logger'),
        ),
        migrations.AddField(
            model_name='temperaturelogger',
            name='HPO6',
            field=models.ForeignKey(to='monitor.TempHPOut6Logger'),
        ),
        migrations.AddField(
            model_name='heatpump6logger',
            name='tempIn',
            field=models.ForeignKey(to='monitor.TempHPIn6Logger'),
        ),
        migrations.AddField(
            model_name='heatpump6logger',
            name='tempOut',
            field=models.ForeignKey(to='monitor.TempHPOut6Logger'),
        ),
        migrations.AddField(
            model_name='heatpump5logger',
            name='tempIn',
            field=models.ForeignKey(to='monitor.TempHPIn5Logger'),
        ),
        migrations.AddField(
            model_name='heatpump5logger',
            name='tempOut',
            field=models.ForeignKey(to='monitor.TempHPOut5Logger'),
        ),
        migrations.AddField(
            model_name='heatpump4logger',
            name='tempIn',
            field=models.ForeignKey(to='monitor.TempHPIn4Logger'),
        ),
        migrations.AddField(
            model_name='heatpump4logger',
            name='tempOut',
            field=models.ForeignKey(to='monitor.TempHPOut4Logger'),
        ),
        migrations.AddField(
            model_name='heatpump3logger',
            name='tempIn',
            field=models.ForeignKey(to='monitor.TempHPIn3Logger'),
        ),
        migrations.AddField(
            model_name='heatpump3logger',
            name='tempOut',
            field=models.ForeignKey(to='monitor.TempHPOut3Logger'),
        ),
        migrations.AddField(
            model_name='heatpump2logger',
            name='tempIn',
            field=models.ForeignKey(to='monitor.TempHPIn2Logger'),
        ),
        migrations.AddField(
            model_name='heatpump2logger',
            name='tempOut',
            field=models.ForeignKey(to='monitor.TempHPOut2Logger'),
        ),
        migrations.AddField(
            model_name='heatpump1logger',
            name='tempIn',
            field=models.ForeignKey(to='monitor.TempHPIn1Logger'),
        ),
        migrations.AddField(
            model_name='heatpump1logger',
            name='tempOut',
            field=models.ForeignKey(to='monitor.TempHPOut1Logger'),
        ),
    ]
