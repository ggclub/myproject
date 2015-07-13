# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0016_floor1ciu1_floor1ciu10_floor1ciu11_floor1ciu12_floor1ciu13_floor1ciu14_floor1ciu2_floor1ciu3_floor1c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor1ciu1',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu1',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu1',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu10',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu10',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu10',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu11',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu11',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu11',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu12',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu12',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu12',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu13',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu13',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu13',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu14',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu14',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu14',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu2',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu2',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu2',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu3',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu3',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu3',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu4',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu4',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu4',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu5',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu5',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu5',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu6',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu6',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu6',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu7',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu7',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu7',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu8',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu8',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu8',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu9',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu9',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor1ciu9',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu1',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu1',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu1',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu10',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu10',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu10',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu11',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu11',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu11',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu12',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu12',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu12',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu2',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu2',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu2',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu3',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu3',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu3',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu4',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu4',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu4',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu5',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu5',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu5',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu6',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu6',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu6',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu7',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu7',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu7',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu8',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu8',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu8',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu9',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu9',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor2ciu9',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu1',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu1',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu1',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu10',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu10',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu10',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu11',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu11',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu11',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu12',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu12',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu12',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu2',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu2',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu2',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu3',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu3',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu3',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu4',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu4',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu4',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu5',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu5',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu5',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu6',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu6',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu6',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu7',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu7',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu7',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu8',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu8',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu8',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu9',
            name='airFlow',
            field=models.CharField(default=b'ST', max_length=2, choices=[(b'WK', b'\xec\x95\xbd\xed\x92\x8d'), (b'NM', b'\xec\xa4\x91\xed\x92\x8d'), (b'ST', b'\xea\xb0\x95\xed\x92\x8d')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu9',
            name='opMode',
            field=models.CharField(default=b'AT', max_length=2, choices=[(b'CL', b'\xeb\x83\x89\xeb\xb0\xa9'), (b'HT', b'\xeb\x82\x9c\xeb\xb0\xa9'), (b'AR', b'\xec\x86\xa1\xed\x92\x8d'), (b'AT', b'\xec\x9e\x90\xeb\x8f\x99')]),
        ),
        migrations.AlterField(
            model_name='floor3ciu9',
            name='state',
            field=models.CharField(default=b'NM', max_length=2, choices=[(b'ER', b'\xec\x97\x90\xeb\x9f\xac'), (b'NM', b'\xec\xa0\x95\xec\x83\x81')]),
        ),
    ]
