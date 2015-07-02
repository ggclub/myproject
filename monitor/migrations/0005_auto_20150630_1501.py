# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_remove_dwpflowmeterlogger_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inverterlogger',
            name='Hz',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
