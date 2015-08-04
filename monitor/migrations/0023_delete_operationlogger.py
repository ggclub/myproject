# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0022_auto_20150721_1009'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OperationLogger',
        ),
    ]
