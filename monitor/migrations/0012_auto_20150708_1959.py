# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_auto_20150708_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powerconsumptionlogger',
            name='currentPowerConsumption',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='powerconsumptionlogger',
            name='integralPowerConsumption',
            field=models.FloatField(),
        ),
    ]
