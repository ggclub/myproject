# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20150629_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpflowmeterlogger',
            name='temperature',
        ),
    ]
