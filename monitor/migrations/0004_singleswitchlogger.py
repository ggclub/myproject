# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20150609_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleSwitchLogger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=4, choices=[(b'HP1', b'Heat Pump-1'), (b'HP2', b'Heat Pump-2'), (b'HP3', b'Heat Pump-3'), (b'HP4', b'Heat Pump-4'), (b'HP5', b'Heat Pump-5'), (b'HP6', b'Heat Pump-6'), (b'DWP1', b'Deep-well Pump-1'), (b'DWP2', b'Deep-well Pump-2'), (b'DWP3', b'Deep-well Pump-3'), (b'DWP4', b'Deep-well Pump-4'), (b'CP1', b'Circulating Pump 1'), (b'CP2', b'Circulating Pump 2')])),
                ('switch', models.CharField(max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')])),
            ],
        ),
    ]
