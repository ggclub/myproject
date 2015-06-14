# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20150609_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flowmeterlogger',
            old_name='DPW',
            new_name='DWP',
        ),
    ]
