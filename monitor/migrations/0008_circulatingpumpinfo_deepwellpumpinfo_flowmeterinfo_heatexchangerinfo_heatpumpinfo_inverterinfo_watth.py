# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_auto_20150630_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='CirculatingPumpInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('flux', models.CharField(max_length=15)),
                ('suction', models.CharField(max_length=15)),
                ('motorHP', models.CharField(max_length=15)),
                ('maxPressure', models.CharField(max_length=60)),
                ('motor', models.CharField(max_length=15)),
                ('voltage', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=15)),
                ('quantity', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DeepWellPumpInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('volume', models.CharField(max_length=15)),
                ('output', models.CharField(max_length=25)),
                ('power', models.CharField(max_length=25)),
                ('height', models.CharField(max_length=15)),
                ('length', models.CharField(max_length=15)),
                ('diameter', models.CharField(max_length=15)),
                ('quantity', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FlowmeterInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=15)),
                ('measureGauge', models.CharField(max_length=15)),
                ('inputPower', models.CharField(max_length=30)),
                ('quantity', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HeatExchangerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('maxPressure', models.CharField(max_length=15)),
                ('tempRange', models.CharField(max_length=15)),
                ('quantity', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HeatPumpInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('voltage', models.CharField(max_length=30)),
                ('capacity', models.CharField(max_length=15)),
                ('refrigerant', models.CharField(max_length=15)),
                ('size', models.CharField(max_length=30)),
                ('weight', models.CharField(max_length=15)),
                ('quantity', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InverterInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('size', models.CharField(max_length=15)),
                ('motorHP', models.CharField(max_length=20)),
                ('ratedCapacity', models.CharField(max_length=15)),
                ('ratedCurrent', models.CharField(max_length=15)),
                ('frequency', models.CharField(max_length=15)),
                ('maxVoltage', models.CharField(max_length=25)),
                ('power', models.CharField(max_length=50)),
                ('coolingSystem', models.CharField(max_length=25)),
                ('quantity', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WattHourMeterInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('size', models.CharField(max_length=40)),
                ('ratedVoltage', models.CharField(max_length=25)),
                ('ratedCurrent', models.CharField(max_length=15)),
                ('accuracy', models.CharField(max_length=25)),
                ('constant', models.CharField(max_length=25)),
                ('outputPulse', models.CharField(max_length=25)),
                ('pulseSpec', models.CharField(max_length=100)),
                ('powerConsumption', models.CharField(max_length=15)),
                ('quantity', models.SmallIntegerField()),
            ],
        ),
    ]
