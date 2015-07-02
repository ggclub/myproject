# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_auto_20150630_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationswitchcontrol',
            name='switch',
            field=models.CharField(max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off'), (b'N/A', b'n/a')]),
        ),
    ]
