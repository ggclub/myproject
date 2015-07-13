# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0018_auto_20150710_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor1CIUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u1', models.ForeignKey(to='monitor.Floor1CIU1')),
                ('u10', models.ForeignKey(to='monitor.Floor1CIU10')),
                ('u11', models.ForeignKey(to='monitor.Floor1CIU11')),
                ('u12', models.ForeignKey(to='monitor.Floor1CIU12')),
                ('u13', models.ForeignKey(to='monitor.Floor1CIU13')),
                ('u14', models.ForeignKey(to='monitor.Floor1CIU14')),
                ('u2', models.ForeignKey(to='monitor.Floor1CIU2')),
                ('u3', models.ForeignKey(to='monitor.Floor1CIU3')),
                ('u4', models.ForeignKey(to='monitor.Floor1CIU4')),
                ('u5', models.ForeignKey(to='monitor.Floor1CIU5')),
                ('u6', models.ForeignKey(to='monitor.Floor1CIU6')),
                ('u7', models.ForeignKey(to='monitor.Floor1CIU7')),
                ('u8', models.ForeignKey(to='monitor.Floor1CIU8')),
                ('u9', models.ForeignKey(to='monitor.Floor1CIU9')),
            ],
        ),
        migrations.CreateModel(
            name='Floor2CIUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u1', models.ForeignKey(to='monitor.Floor2CIU1')),
                ('u10', models.ForeignKey(to='monitor.Floor2CIU10')),
                ('u11', models.ForeignKey(to='monitor.Floor2CIU11')),
                ('u12', models.ForeignKey(to='monitor.Floor2CIU12')),
                ('u2', models.ForeignKey(to='monitor.Floor2CIU2')),
                ('u3', models.ForeignKey(to='monitor.Floor2CIU3')),
                ('u4', models.ForeignKey(to='monitor.Floor2CIU4')),
                ('u5', models.ForeignKey(to='monitor.Floor2CIU5')),
                ('u6', models.ForeignKey(to='monitor.Floor2CIU6')),
                ('u7', models.ForeignKey(to='monitor.Floor2CIU7')),
                ('u8', models.ForeignKey(to='monitor.Floor2CIU8')),
                ('u9', models.ForeignKey(to='monitor.Floor2CIU9')),
            ],
        ),
        migrations.CreateModel(
            name='Floor3CIUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u1', models.ForeignKey(to='monitor.Floor3CIU1')),
                ('u10', models.ForeignKey(to='monitor.Floor3CIU10')),
                ('u11', models.ForeignKey(to='monitor.Floor3CIU11')),
                ('u12', models.ForeignKey(to='monitor.Floor3CIU12')),
                ('u2', models.ForeignKey(to='monitor.Floor3CIU2')),
                ('u3', models.ForeignKey(to='monitor.Floor3CIU3')),
                ('u4', models.ForeignKey(to='monitor.Floor3CIU4')),
                ('u5', models.ForeignKey(to='monitor.Floor3CIU5')),
                ('u6', models.ForeignKey(to='monitor.Floor3CIU6')),
                ('u7', models.ForeignKey(to='monitor.Floor3CIU7')),
                ('u8', models.ForeignKey(to='monitor.Floor3CIU8')),
                ('u9', models.ForeignKey(to='monitor.Floor3CIU9')),
            ],
        ),
    ]
