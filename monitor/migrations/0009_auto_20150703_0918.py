# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0008_circulatingpumpinfo_deepwellpumpinfo_flowmeterinfo_heatexchangerinfo_heatpumpinfo_inverterinfo_watth'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpflowmeterlogger',
            name='temperature',
            field=models.FloatField(default=13.4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dwpflowmeterlogger',
            name='temperature',
            field=models.FloatField(default=12.1),
            preserve_default=False,
        ),
    ]
