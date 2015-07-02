from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
	help = 'watch file in share dir.'

	def handle(self, *args, **options):
		self.stdout.write('cmd test.py')
		# self.stdout.write('args: '+str(args) + ', options: ' + str(options))
		watch()
		self.stdout.write('end of handle')


import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
from django.utils import timezone
from datetime import datetime as dt

from monitor.models import *
import json
from pprint import pprint


class MyHandler(FileSystemEventHandler):
	def on_modified(self, event):
		with open('C:/Users/Admin/Documents/Django/myproject/share/hmidata.json') as data_file:
			data = json.load(data_file)
		
		datetime = data["datetime"]
		datetime = dt.strptime(datetime, "%Y-%m-%d %H:%M:%S")
		if(timezone.now() - datetime < timezone.timedelta(seconds=10)):
		    return

		op_mode=data["op_mode"]

		###### save models
		hei1 = TempHEIn1Logger(temperature=data["hei1"])
		heo1 = TempHEOut1Logger(temperature=data["heo1"])
		hei2 = TempHEIn2Logger(temperature=data["hei2"])
		heo2 = TempHEOut2Logger(temperature=data["heo2"])
		hei1.save(); hei2.save(); heo1.save(); heo1.save();

		hpi1 = TempHPIn1Logger(temperature=data["heo1"])
		hpi2 = TempHPIn2Logger(temperature=data["heo1"])
		hpi3 = TempHPIn3Logger(temperature=data["heo1"])
		hpi4 = TempHPIn4Logger(temperature=data["heo1"])
		hpi5 = TempHPIn5Logger(temperature=data["heo1"])
		hpi6 = TempHPIn6Logger(temperature=data["heo1"])
		hpi1.save();hpi2.save();hpi3.save();hpi4.save();hpi5.save();hpi6.save();

		hpo1 = TempHPOut1Logger(temperature=data["hpo1"])
		hpo2 = TempHPOut2Logger(temperature=data["hpo2"])
		hpo3 = TempHPOut3Logger(temperature=data["hpo3"])
		hpo4 = TempHPOut4Logger(temperature=data["hpo4"])
		hpo5 = TempHPOut5Logger(temperature=data["hpo5"])
		hpo6 = TempHPOut6Logger(temperature=data["hpo6"])
		hpo1.save();hpo2.save();hpo3.save();hpo4.save();hpo5.save();hpo6.save();

		hp1 = HeatPump1Logger(
		    dateTime=datetime, opMode=op_mode, switch=data["hp1"], tempIn=hpi1,tempOut=hpo1
		    )
		hp2 = HeatPump2Logger(
		    dateTime=datetime, opMode=op_mode, switch=data["hp2"], tempIn=hpi2,tempOut=hpo2
		    )
		hp3 = HeatPump3Logger(
		    dateTime=datetime, opMode=op_mode, switch=data["hp3"], tempIn=hpi3,tempOut=hpo3
		    )
		hp4 = HeatPump4Logger(
		    dateTime=datetime, opMode=op_mode, switch=data["hp4"], tempIn=hpi4,tempOut=hpo4
		    )
		hp5 = HeatPump5Logger(
		    dateTime=datetime, opMode=op_mode, switch=data["hp5"], tempIn=hpi5,tempOut=hpo5
		    )
		hp6 = HeatPump6Logger(
		    dateTime=datetime, opMode=op_mode, switch=data["hp6"], tempIn=hpi6,tempOut=hpo6
		    )
		hp1.save();hp2.save();hp3.save();hp4.save();hp5.save();hp6.save()

		dwp1 = DeepwellPump1Logger(
		    dateTime=datetime, opMode=op_mode, switch=data["dwp1"]
		    )
		dwp2 = DeepwellPump2Logger(
		    dateTime=datetime, opMode=op_mode, switch=data["dwp2"]
		    )
		dwp3 = DeepwellPump3Logger(
		    dateTime=datetime, opMode=op_mode, switch=data["dwp3"]
		    )
		dwp4 = DeepwellPump4Logger(
		    dateTime=datetime, opMode=op_mode, switch=data["dwp4"]
		    )
		dwp1.save();dwp2.save();dwp3.save();dwp4.save();

		cp = CirculatingPumpLogger(
			dateTime=datetime, CPID=data["cp_id"], opMode=op_mode, switch=data["cp"]
			)
		cp.save()

		inverter = InverterLogger(
			dateTime=datetime, inverterID=data["cp_id"], opMode=op_mode, switch=data["cp"], RPM=data["cp_rpm"], Hz=data["inverter_hz"]
			)
		inverter.save()

		dwpfm = DWPFlowmeterLogger(
		    dateTime=datetime, currentFlux=data["dwpfm_cur"], integralFlux=data["dwpfm_int"]
		    )
		cpfm = CPFlowmeterLogger(
		    dateTime=datetime, currentFlux=data["cpfm_cur"], integralFlux=data["cpfm_int"]
		    )
		dwpfm.save();cpfm.save();

		power = PowerConsumptionLogger(
		    dateTime=datetime, currentPowerConsumption=data["pow_cur"], integralPowerConsumption=data["pow_int"]
		    )
		power.save()

		print 'data updated'


def watch():
	observer = Observer()
	observer.schedule(MyHandler(), path='C:/Users/Admin/Documents/Django/myproject/share')#args[0] if args else '.')
	observer.start()

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()

	observer.join()
