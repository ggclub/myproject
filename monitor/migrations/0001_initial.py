# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlowmeterLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('DWP', models.SmallIntegerField()),
                ('CP', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OperationLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('mode', models.CharField(default=b'AT', max_length=2, choices=[(b'MN', b'Manual'), (b'AT', b'Auto')])),
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
            ],
        ),
        migrations.CreateModel(
            name='SingleSwitchLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=4, choices=[(b'HP1', b'Heat Pump-1'), (b'HP2', b'Heat Pump-2'), (b'HP3', b'Heat Pump-3'), (b'HP4', b'Heat Pump-4'), (b'HP5', b'Heat Pump-5'), (b'HP6', b'Heat Pump-6'), (b'DWP1', b'Deep-well Pump-1'), (b'DWP2', b'Deep-well Pump-2'), (b'DWP3', b'Deep-well Pump-3'), (b'DWP4', b'Deep-well Pump-4'), (b'CP1', b'Circulating Pump 1'), (b'CP2', b'Circulating Pump 2')])),
                ('switch', models.CharField(max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('HPI1', models.FloatField()),
                ('HPO1', models.FloatField()),
                ('HPI2', models.FloatField()),
                ('HPO2', models.FloatField()),
                ('HPI3', models.FloatField()),
                ('HPO3', models.FloatField()),
                ('HPI4', models.FloatField()),
                ('HPO4', models.FloatField()),
                ('HPI5', models.FloatField()),
                ('HPO5', models.FloatField()),
                ('HPI6', models.FloatField()),
                ('HPO6', models.FloatField()),
            ],
        ),
    ]
