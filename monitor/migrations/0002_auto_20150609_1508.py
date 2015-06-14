# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operationlogger',
            old_name='CP',
            new_name='CP1',
        ),
        migrations.AddField(
            model_name='operationlogger',
            name='CP2',
            field=models.CharField(default=b'OFF', max_length=3, choices=[(b'ON', b'On'), (b'OFF', b'Off')]),
        ),
    ]
