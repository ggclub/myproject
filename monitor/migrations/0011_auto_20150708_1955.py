# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0010_auto_20150707_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpflowmeterlogger',
            name='velocity',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dwpflowmeterlogger',
            name='velocity',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
