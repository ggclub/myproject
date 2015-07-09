# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0012_auto_20150708_1959'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InverterLogger',
        ),
        migrations.AddField(
            model_name='circulatingpumplogger',
            name='Flux',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circulatingpumplogger',
            name='Hz',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
