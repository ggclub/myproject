# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0023_delete_operationlogger'),
    ]

    operations = [
        migrations.CreateModel(
            name='CiuOnHeatPump1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u1', models.ForeignKey(to='monitor.Floor3CIU9')),
                ('u2', models.ForeignKey(to='monitor.Floor3CIU10')),
                ('u3', models.ForeignKey(to='monitor.Floor3CIU11')),
                ('u4', models.ForeignKey(to='monitor.Floor3CIU12')),
            ],
        ),
        migrations.CreateModel(
            name='CiuOnHeatPump2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u1', models.ForeignKey(to='monitor.Floor2CIU8')),
                ('u2', models.ForeignKey(to='monitor.Floor2CIU9')),
                ('u3', models.ForeignKey(to='monitor.Floor2CIU10')),
                ('u4', models.ForeignKey(to='monitor.Floor2CIU11')),
                ('u5', models.ForeignKey(to='monitor.Floor2CIU12')),
            ],
        ),
        migrations.CreateModel(
            name='CiuOnHeatPump3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u1', models.ForeignKey(to='monitor.Floor2CIU2')),
                ('u2', models.ForeignKey(to='monitor.Floor2CIU3')),
                ('u3', models.ForeignKey(to='monitor.Floor2CIU4')),
                ('u4', models.ForeignKey(to='monitor.Floor2CIU5')),
                ('u5', models.ForeignKey(to='monitor.Floor2CIU6')),
                ('u6', models.ForeignKey(to='monitor.Floor2CIU7')),
            ],
        ),
        migrations.CreateModel(
            name='CiuOnHeatPump4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u1', models.ForeignKey(to='monitor.Floor1CIU1')),
                ('u2', models.ForeignKey(to='monitor.Floor1CIU2')),
                ('u3', models.ForeignKey(to='monitor.Floor1CIU3')),
                ('u4', models.ForeignKey(to='monitor.Floor1CIU4')),
                ('u5', models.ForeignKey(to='monitor.Floor1CIU5')),
                ('u6', models.ForeignKey(to='monitor.Floor2CIU1')),
                ('u7', models.ForeignKey(to='monitor.Floor3CIU1')),
            ],
        ),
        migrations.CreateModel(
            name='CiuOnHeatPump5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u1', models.ForeignKey(to='monitor.Floor1CIU6')),
                ('u2', models.ForeignKey(to='monitor.Floor1CIU7')),
                ('u3', models.ForeignKey(to='monitor.Floor1CIU8')),
                ('u4', models.ForeignKey(to='monitor.Floor1CIU9')),
                ('u5', models.ForeignKey(to='monitor.Floor1CIU10')),
                ('u6', models.ForeignKey(to='monitor.Floor1CIU11')),
                ('u7', models.ForeignKey(to='monitor.Floor1CIU12')),
                ('u8', models.ForeignKey(to='monitor.Floor1CIU13')),
                ('u9', models.ForeignKey(to='monitor.Floor1CIU14')),
            ],
        ),
        migrations.CreateModel(
            name='CiuOnHeatPump6',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u1', models.ForeignKey(to='monitor.Floor3CIU2')),
                ('u2', models.ForeignKey(to='monitor.Floor3CIU3')),
                ('u3', models.ForeignKey(to='monitor.Floor3CIU4')),
                ('u4', models.ForeignKey(to='monitor.Floor3CIU5')),
                ('u5', models.ForeignKey(to='monitor.Floor3CIU6')),
                ('u6', models.ForeignKey(to='monitor.Floor3CIU7')),
                ('u7', models.ForeignKey(to='monitor.Floor3CIU8')),
            ],
        ),
    ]
