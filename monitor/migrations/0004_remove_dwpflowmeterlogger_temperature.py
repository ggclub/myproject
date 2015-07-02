# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_remove_cpflowmeterlogger_temperature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dwpflowmeterlogger',
            name='temperature',
        ),
    ]
