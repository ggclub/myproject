# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0013_auto_20150708_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='circulatingpumplogger',
            old_name='Flux',
            new_name='flux',
        ),
    ]
