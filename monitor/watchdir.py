# if __name__ == '__main__' and __package__ is None:
#     export DJANGO_SETTINGS_MODULE=mysite.settings
#     import sys, os.path
#     sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
from django.utils import timezone

from models import *
import json
from pprint import pprint


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with open('C:/Users/Admin/Documents/Django/myproject/share/hmidata.json') as data_file:
            data = json.load(data_file)
        pprint (data)
        datetime = data["datetime"]
        datetime = timezone.strptime(datetime, "%Y-%m-%d %H:%M:%S")
        if(timezone.now() - datetime > timezone.timedelta(seconds=10)):
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
        hpi1.save();hpi2.save()hpi3.save();hpi4.save();hpi5.save();hpi6.save();
        
        hpo1 = TempHPOut1Logger(temperature=data["hpo1"])
        hpo2 = TempHPOut2Logger(temperature=data["hpo2"])
        hpo3 = TempHPOut3Logger(temperature=data["hpo3"])
        hpo4 = TempHPOut4Logger(temperature=data["hpo4"])
        hpo5 = TempHPOut5Logger(temperature=data["hpo5"])
        hpo6 = TempHPOut6Logger(temperature=data["hpo6"])
        hpo1.save();hpo2.save();hpo3.save();hpo4.save();hpo5.save();hpo6.save();

        hp1 = HeatPump1Logger(
            dateTime=datetime, opMode=op_mode, switch=data["hp1"], tempIn=data["heo1"],tempOut=data["hpo1"]
            )
        hp2 = HeatPump2Logger(
            dateTime=datetime, opMode=op_mode, switch=data["hp2"], tempIn=data["heo1"],tempOut=data["hpo2"]
            )
        hp3 = HeatPump3Logger(
            dateTime=datetime, opMode=op_mode, switch=data["hp3"], tempIn=data["heo1"],tempOut=data["hpo3"]
            )
        hp4 = HeatPump4Logger(
            dateTime=datetime, opMode=op_mode, switch=data["hp4"], tempIn=data["heo1"],tempOut=data["hpo4"]
            )
        hp5 = HeatPump5Logger(
            dateTime=datetime, opMode=op_mode, switch=data["hp5"], tempIn=data["heo1"],tempOut=data["hpo5"]
            )
        hp6 = HeatPump6Logger(
            dateTime=datetime, opMode=op_mode, switch=data["hp6"], tempIn=data["heo1"],tempOut=data["hpo6"]
            )
        hp1.save();hp2.save();hp3.save();hp4.save();

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


        # print "dwp1 : " + data["dwp1"]
        # print "op_mode : " + data["op_mode"]
        # print "Got it!"





def file_watch(filepath):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=filepath, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path='C:/Users/Admin/Documents/Django/myproject/share')#args[0] if args else '.')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


# import sys
# import time
# import xmltodict
# import magicdate
# from watchdog.observers import Observer
# from watchdog.events import PatternMatchingEventHandler


# class MyHandler(PatternMatchingEventHandler):
#     patterns=["*.xml"]

#     def process(self, event):
#         """
#         event.event_type
#             'modified' | 'created' | 'moved' | 'deleted'
#         event.is_directory
#             True | False
#         event.src_path
#             path/to/observed/file
#         """

#         with open(event.src_path, 'r') as xml_source:
#             xml_string = xml_source.read()
#             parsed = xmltodict.parse(xml_string)
#             element = parsed.get('Pulsar', {}).get('OnAir', {}).get('media')
#             if not element:
#                 return

#             media = Media(
#                 title=element.get('title1'),
#                 description=element.get('title3'),
#                 media_id=element.get('media_id1'),
#                 hour=magicdate(element.get('hour')),
#                 length=element.get('title4')
#             )
#             media.save()

#     def on_modified(self, event):
#         self.process(event)

#     def on_created(self, event):
#         self.process(event)

