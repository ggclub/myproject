# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deepwellpump1logger',
            name='waterLevel',
            field=models.CharField(default=b'AP', max_length=2, choices=[(b'AP', b'\xec\xa0\x81\xec\xa0\x95'), (b'NA', b'\xeb\xb6\x80\xec\xa0\x81\xec\xa0\x95')]),
        ),
        migrations.AlterField(
            model_name='deepwellpump2logger',
            name='waterLevel',
            field=models.CharField(default=b'AP', max_length=2, choices=[(b'AP', b'\xec\xa0\x81\xec\xa0\x95'), (b'NA', b'\xeb\xb6\x80\xec\xa0\x81\xec\xa0\x95')]),
        ),
        migrations.AlterField(
            model_name='deepwellpump3logger',
            name='waterLevel',
            field=models.CharField(default=b'AP', max_length=2, choices=[(b'AP', b'\xec\xa0\x81\xec\xa0\x95'), (b'NA', b'\xeb\xb6\x80\xec\xa0\x81\xec\xa0\x95')]),
        ),
        migrations.AlterField(
            model_name='deepwellpump4logger',
            name='waterLevel',
            field=models.CharField(default=b'AP', max_length=2, choices=[(b'AP', b'\xec\xa0\x81\xec\xa0\x95'), (b'NA', b'\xeb\xb6\x80\xec\xa0\x81\xec\xa0\x95')]),
        ),
    ]
