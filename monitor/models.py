	
#-*- coding: utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone


SWITCH_CHOICES = (
	('ON', 'On'),
	('OFF', 'Off'),
)

MANUAL = 'MN'
AUTO = 'AT'
OPMODE_CHOICES = (
	(MANUAL, '수동'),
	(AUTO, '자동'),
)

# switch control
class OperationSwitchControl(models.Model):
	dateTime = models.DateTimeField()
	LOCATION_CHOICES = (
		('HP1', '히트 펌프 1'),
		('HP2', '히트 펌프 2'),
		('HP3', '히트 펌프 3'),
		('HP4', '히트 펌프 4'),
		('HP5', '히트 펌프 5'),
		('HP6', '히트 펌프 6'),
		('DWP1', '심정 펌프 1'),
		('DWP2', '심정 펌프 2'),
		('DWP3', '심정 펌프 3'),
		('DWP4', '심정 펌프 4'),
		('CP1', '순환 펌프 1'),
		('CP2', '순환 펌프 2'),
		('IV', '인버터'),
	)
	location = models.CharField(max_length=4, choices=LOCATION_CHOICES)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES)
	def __str__(self):
		return '{}, location: {}: {}'.format(self.dateTime, self.location, self.switch)


class OperationLogger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)

	COOL='CL'
	HEAT='HT'
	TEMPMODE_CHOICES = (
		(COOL, '냉방'),
		(HEAT, '난방'),
	)
	tempMode = models.CharField(max_length=2, choices=TEMPMODE_CHOICES, default=AUTO)
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
	Inverter = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF')
	def __str__(self):
		return str(self.dateTime)


# pump
APPROPRIATE='AP'
NOTAPPROPRIATE='NA'
WATERLEVEL_CHOICES = (
	(APPROPRIATE, '적정'),
	(NOTAPPROPRIATE, '부적정'),
)
class DeepwellPump1Logger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 	
	waterLevel = models.CharField(max_length=2, choices=WATERLEVEL_CHOICES, default="")
	def __str__(self):
		return '{}: {}-{}'.format(self.dateTime, self.opMode, self.switch)

class DeepwellPump2Logger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 	
	waterLevel = models.CharField(max_length=2, choices=WATERLEVEL_CHOICES, default="")
	def __str__(self):
		return '{}: {}-{}'.format(self.dateTime, self.opMode, self.switch)

class DeepwellPump3Logger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 	
	waterLevel = models.CharField(max_length=2, choices=WATERLEVEL_CHOICES, default="")
	def __str__(self):
		return '{}: {}-{}'.format(self.dateTime, self.opMode, self.switch)

class DeepwellPump4Logger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 	
	waterLevel = models.CharField(max_length=2, choices=WATERLEVEL_CHOICES, default="")
	def __str__(self):
		return '{}: {}-{}'.format(self.dateTime, self.opMode, self.switch)

class CirculatingPumpLogger(models.Model):
	dateTime = models.DateTimeField()
	CP_ID_CHOICES = (
		(1, '1'),
		(2, '2'),
	)
	CPID = models.SmallIntegerField(choices=CP_ID_CHOICES, default=1)
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 
	def __str__(self):
		return '{}, {}-{}'.format(self.dateTime, self.opMode, self.switch)


# flowmeter
class DWPFlowmeterLogger(models.Model):
	dateTime = models.DateTimeField()
	temperature = models.FloatField()
	currentFlux = models.SmallIntegerField()
	integralFlux = models.IntegerField()
	def __str__(self):
		return '{}, current: {}'.format(self.dateTime, self.currentFlux)

class CPFlowmeterLogger(models.Model):
	dateTime = models.DateTimeField()
	temperature = models.FloatField()
	currentFlux = models.SmallIntegerField()
	integralFlux = models.IntegerField()
	def __str__(self):
		return '{}, current: {}'.format(self.dateTime, self.currentFlux)



class TempHEIn1Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHEOut1Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHEIn2Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHEOut2Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPIn1Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPOut1Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPIn2Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPOut2Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPIn3Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPOut3Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPIn4Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPOut4Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPIn5Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPOut5Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPIn6Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)

class TempHPOut6Logger(models.Model):
	temperature = models.FloatField(default=0.0)
	def __str__(self):
		return str(self.temperature)


def get_HPI1():
	return TempHPIn1Logger.objects.latest('temperature')
def get_HPO1():
	return TempHPOut1Logger.objects.latest('temperature')
def get_HPI2():
	return TemperatureLogger.objects.latest('dateTime').HPI2
def get_HPO2():
	return TemperatureLogger.objects.latest('dateTime').HPO2
def get_HPI3():
	return TemperatureLogger.objects.latest('dateTime').HPI3
def get_HPO3():
	return TemperatureLogger.objects.latest('dateTime').HPO3
def get_HPI4():
	return TemperatureLogger.objects.latest('dateTime').HPI4
def get_HPO4():
	return TemperatureLogger.objects.latest('dateTime').HPO4
def get_HPI5():
	return TemperatureLogger.objects.latest('dateTime').HPI5
def get_HPO5():
	return TemperatureLogger.objects.latest('dateTime').HPO5
def get_HPI6():
	return TemperatureLogger.objects.latest('dateTime').HPI6
def get_HPO6():
	return TemperatureLogger.objects.latest('dateTime').HPO6

# thermometer
class TemperatureLogger(models.Model):
	dateTime = models.DateTimeField()
	HEI1 = models.ForeignKey(TempHEIn1Logger)
	HEO1 = models.ForeignKey(TempHEOut1Logger)
	HEI2 = models.ForeignKey(TempHEIn2Logger)
	HEO2 = models.ForeignKey(TempHEOut2Logger)
	HPI1 = models.ForeignKey(TempHPIn1Logger)
	HPO1 = models.ForeignKey(TempHPOut1Logger)
	HPI2 = models.ForeignKey(TempHPIn2Logger)
	HPO2 = models.ForeignKey(TempHPOut2Logger)
	HPI3 = models.ForeignKey(TempHPIn3Logger)
	HPO3 = models.ForeignKey(TempHPOut3Logger)
	HPI4 = models.ForeignKey(TempHPIn4Logger)
	HPO4 = models.ForeignKey(TempHPOut4Logger)
	HPI5 = models.ForeignKey(TempHPIn5Logger)
	HPO5 = models.ForeignKey(TempHPOut5Logger)
	HPI6 = models.ForeignKey(TempHPIn6Logger)
	HPO6 = models.ForeignKey(TempHPOut6Logger)
	def __str__(self):
		return str(self.dateTime)





# inverter
class InverterLogger(models.Model):
	dateTime = models.DateTimeField()
	INVERTER_ID_CHOICES = (
		(1, 'Inverter1'),
		(2, 'Inverter2'),
	)
	inverterID = models.SmallIntegerField(choices=INVERTER_ID_CHOICES, default=1)
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 
	RPM = models.SmallIntegerField()
	Hz = models.FloatField(null=True, blank=True)
	def __str__(self):
		return '{}, {}-{}, RPM: {}'.format(self.dateTime, self.opMode, self.switch, self.RPM)


# heat pump
class HeatPump1Logger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 
	tempIn = models.ForeignKey(TempHPIn1Logger)
	tempOut = models.ForeignKey(TempHPOut1Logger)
	def __str__(self):
		return '{}, {}'.format(self.dateTime, self.switch)

class HeatPump2Logger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 
	tempIn = models.ForeignKey(TempHPIn2Logger)
	tempOut = models.ForeignKey(TempHPOut2Logger)
	def __str__(self):
		return '{}, {}'.format(self.dateTime, self.switch)

class HeatPump3Logger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 
	tempIn = models.ForeignKey(TempHPIn3Logger)
	tempOut = models.ForeignKey(TempHPOut3Logger)
	def __str__(self):
		return '{}, {}'.format(self.dateTime, self.switch)

class HeatPump4Logger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 
	tempIn = models.ForeignKey(TempHPIn4Logger)
	tempOut = models.ForeignKey(TempHPOut4Logger)
	def __str__(self):
		return '{}, {}'.format(self.dateTime, self.switch)

class HeatPump5Logger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 
	tempIn = models.ForeignKey(TempHPIn5Logger)
	tempOut = models.ForeignKey(TempHPOut5Logger)
	def __str__(self):
		return '{}, {}'.format(self.dateTime, self.switch)

class HeatPump6Logger(models.Model):
	dateTime = models.DateTimeField()
	opMode = models.CharField(max_length=2, choices=OPMODE_CHOICES, default=AUTO)
	switch = models.CharField(max_length=3, choices=SWITCH_CHOICES, default='OFF') 
	tempIn = models.ForeignKey(TempHPIn6Logger)
	tempOut = models.ForeignKey(TempHPOut6Logger)
	def __str__(self):
		return '{}, {}'.format(self.dateTime, self.switch)


# power consumption
class PowerConsumptionLogger(models.Model):
	dateTime = models.DateTimeField()
	currentPowerConsumption = models.IntegerField()
	integralPowerConsumption = models.IntegerField()
	def __str__(self):
		return '{}, current: {}'.format(self.dateTime, self.currentPowerConsumption)


# refrigeration ton
class RefrigerationTonLogger(models.Model):
	dateTime = models.DateTimeField()
	RT = models.SmallIntegerField()
	def __str__(self):
		return '{}, RT: {}'.format(self.dateTime, self.RT)


# tube well 
class TubeWellLogger(models.Model):
	T1level = models.FloatField()
	T1temp = models.FloatField()
	T2level = models.FloatField()
	T2temp = models.FloatField()
	T3level = models.FloatField()
	T3temp = models.FloatField()
	T4level = models.FloatField()
	T4temp = models.FloatField()


