# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0009_auto_20150703_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refrigerationtonlogger',
            name='RT',
            field=models.FloatField(),
        ),
    ]
