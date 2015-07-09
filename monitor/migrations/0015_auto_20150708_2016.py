# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0014_auto_20150708_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circulatingpumplogger',
            name='Hz',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='circulatingpumplogger',
            name='flux',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cpflowmeterlogger',
            name='velocity',
            field=models.FloatField(default=0),
        ),
    ]
