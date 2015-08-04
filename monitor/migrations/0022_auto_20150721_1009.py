# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0021_auto_20150715_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='temphein1logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 15, 124000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphein2logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 20, 149000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempheout1logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 24, 254000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempheout2logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 28, 92000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpin1logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 31, 727000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpin2logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 33, 412000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpin3logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 35, 174000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpin4logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 36, 875000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpin5logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 38, 560000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpin6logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 40, 229000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpout1logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 41, 758000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpout2logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 43, 68000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpout3logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 44, 316000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpout4logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 45, 642000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpout5logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 46, 999000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphpout6logger',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 9, 48, 421000)),
            preserve_default=False,
        ),
    ]
