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
	CP1 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	CP2 = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')

	def __str__(self):
		return str(self.date)


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

	def __str__(self):
		return str(self.date)


class FlowmeterLogger(models.Model):
	date = models.DateTimeField()
	DWP = models.SmallIntegerField()
	CP = models.SmallIntegerField()

	def __str__(self):
		return str(self.date)


class SingleSwitchLogger(models.Model):
	date = models.DateTimeField()
	LOCATION_CHOICES = (
		('HP1', 'Heat Pump-1'),
		('HP2', 'Heat Pump-2'),
		('HP3', 'Heat Pump-3'),
		('HP4', 'Heat Pump-4'),
		('HP5', 'Heat Pump-5'),
		('HP6', 'Heat Pump-6'),
		('DWP1', 'Deep-well Pump-1'),
		('DWP2', 'Deep-well Pump-2'),
		('DWP3', 'Deep-well Pump-3'),
		('DWP4', 'Deep-well Pump-4'),
		('CP1', 'Circulating Pump 1'),
		('CP2', 'Circulating Pump 2'),
	)
	location = models.CharField(max_length=4, choices=LOCATION_CHOICES)

	SWITCH_CHOICES = (
		('ON', 'On'),
		('OFF', 'Off'),
	)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES)

	def __str__(self):
		return str(self.date)
