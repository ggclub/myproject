import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class OperationLogger(models.Model):
	date = models.DateTimeField()
	
	MANUAL = 'MN'
	AUTO = 'AT'
	MODE_CHOICES = (
		(MANUAL, 'Manual'),
		(AUTO, 'Auto'),
	)
	mode = models.CharField(max_length=2, choices=MODE_CHOICES, default=AUTO)

	SWITCH_CHOICES = (
		('ON', 'On'),
		('OFF', 'Off'),
	)
	HP1 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	HP2 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	HP3 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	HP4 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	HP5 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	HP6 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	DWP1 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	DWP2 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	DWP3 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	DWP4 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	CP = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')


class TemperatureLogger(models.Model):
	date = models.DateTimeField()
	HPI1 = models.FloatField()
	HPO1 = models.FloatField()
	HPI2 = models.FloatField()
	HPO2 = models.FloatField()
	HPI3 = models.FloatField()
	HPO3 = models.FloatField()
	HPI4 = models.FloatField()
	HPO4 = models.FloatField()
	HPI5 = models.FloatField()
	HPO5 = models.FloatField()
	HPI6 = models.FloatField()
	HPO6 = models.FloatField()

class FlowmeterLogger(models.Model):
	date = models.DateTimeField()
	DPW = models.SmallIntegerField()
	CP = models.SmallIntegerField()