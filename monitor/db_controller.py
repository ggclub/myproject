#-*- coding: utf-8 -*-
from .models import *

from django.core.paginator import Paginator, EmptyPage
from django.utils import timezone
import simplejson as json
from datetime import datetime as dt

import logging
log = logging.getLogger(__name__)

import os, myproject.settings
file_path = os.path.join(myproject.settings.BASE_DIR, 'share\\')
# 'C:/Users/Admin/Documents/Django/myproject/share/'

prev_section = 'a' 	# a~e
buf_a = 0; buf_b = 0; buf_c = 0; buf_d = 0;
pump_buffer = 1
pump_off_delay = 5
save_interval = 10

def get_operation_log(page):
	logs_per_page = 10
	page_no = 5

	# 기기 동작 내역
	switch_list = OperationSwitchControl.objects.order_by('-dateTime')
	paginator = Paginator(switch_list, logs_per_page)
	
	# 선택된 페이지가 범위를 초과된 경우 (prev, next 선택)
	selected = page
	if (selected <= 1):
		selected = 1
	elif (selected > paginator.num_pages):
		selected = paginator.num_pages

	try:
		switch_logs = paginator.page(selected)
	except EmptyPage:
		# if page is out of range, deliver last page of results.
		switch_logs = paginator.page(paginator.num_pages)

	if (selected-page_no < 0):
		page_range = range(1,10)
	elif (selected + page_no > paginator.num_pages):
		page_range = paginator.page_range[paginator.num_pages-10:]
	else :
		page_range = paginator.page_range[selected-page_no:selected+page_no-1]


	data = {
		"switch_logs": switch_logs,
		"page_range": page_range,
		"selected": selected,
	}
	return data

def get_sensors():
	# db에 저장된 값을 읽어옴
	heat_pump_1 = HeatPump1Logger.objects.latest('id')
	heat_pump_2 = HeatPump2Logger.objects.latest('id')
	heat_pump_3 = HeatPump3Logger.objects.latest('id')
	heat_pump_4 = HeatPump4Logger.objects.latest('id')
	heat_pump_5 = HeatPump5Logger.objects.latest('id')
	heat_pump_6 = HeatPump6Logger.objects.latest('id')
	heat_pump = [
		heat_pump_1,
		heat_pump_2,
		heat_pump_3,
		heat_pump_4,
		heat_pump_5,
		heat_pump_6,
	]

	deepwell_pump_1 = DeepwellPump1Logger.objects.latest('dateTime')
	deepwell_pump_2 = DeepwellPump2Logger.objects.latest('dateTime')
	deepwell_pump_3 = DeepwellPump3Logger.objects.latest('dateTime')
	deepwell_pump_4 = DeepwellPump4Logger.objects.latest('dateTime')
	DWP = [
		deepwell_pump_1,
		deepwell_pump_2,
		deepwell_pump_3,
		deepwell_pump_4,
	]

	circulating_pump = CirculatingPumpLogger.objects.latest('dateTime')

	DWPFM = DWPFlowmeterLogger.objects.latest('dateTime')
	CPFM = CPFlowmeterLogger.objects.latest('dateTime')

	temp_HEIn1 = TempHEIn1Logger.objects.latest('id')
	temp_HEIn2 = TempHEIn2Logger.objects.latest('id')
	temp_HEOut1 = TempHEOut1Logger.objects.latest('id')
	temp_HEOut2 = TempHEOut2Logger.objects.latest('id')
	temp_HPIn1 = TempHPIn1Logger.objects.latest('id')
	temp_HPIn2 = TempHPIn2Logger.objects.latest('id')
	temp_HPIn3 = TempHPIn3Logger.objects.latest('id')
	temp_HPIn4 = TempHPIn4Logger.objects.latest('id')
	temp_HPIn5 = TempHPIn5Logger.objects.latest('id')
	temp_HPIn6 = TempHPIn6Logger.objects.latest('id')
	temp_HPOut1 = TempHPOut1Logger.objects.latest('id')
	temp_HPOut2 = TempHPOut2Logger.objects.latest('id')
	temp_HPOut3 = TempHPOut3Logger.objects.latest('id')
	temp_HPOut4 = TempHPOut4Logger.objects.latest('id')
	temp_HPOut5 = TempHPOut5Logger.objects.latest('id')
	temp_HPOut6 = TempHPOut6Logger.objects.latest('id')
	temp_HE = [
		temp_HEIn1,
		temp_HEOut1,
		temp_HEIn2,
		temp_HEOut2,
	]
	temp_HP = [
		temp_HPIn1,
		temp_HPIn2,
		temp_HPIn3,
		temp_HPIn4,
		temp_HPIn5,
		temp_HPIn6,
		temp_HPOut1,
		temp_HPOut2,
		temp_HPOut3,
		temp_HPOut4,
		temp_HPOut5,
		temp_HPOut6,
	]

	power = PowerConsumptionLogger.objects.latest('dateTime')
	rt = RefrigerationTonLogger.objects.latest('dateTime')
	switch_log = OperationSwitchControl.objects.latest('dateTime')

	data = {
		"heat_pump": heat_pump,
		"DWP": DWP,
		"circulating_pump": circulating_pump,
		"DWPFM": DWPFM,
		"CPFM": CPFM,
		"temp_HE": temp_HE,
		# "temp_HP": temp_HP,
		"temp_HEIn1": temp_HEIn1,
		"temp_HEOut1": temp_HEOut1,
		"temp_HEIn2": temp_HEIn2,
		"temp_HEOut2": temp_HEOut2,
		"temp_HPIn1": temp_HPIn1,
		"temp_HPIn2": temp_HPIn2,
		"temp_HPIn3": temp_HPIn3,
		"temp_HPIn4": temp_HPIn4,
		"temp_HPIn5": temp_HPIn5,
		"temp_HPIn6": temp_HPIn6,
		"temp_HPOut1": temp_HPOut1,
		"temp_HPOut2": temp_HPOut2,
		"temp_HPOut3": temp_HPOut3,
		"temp_HPOut4": temp_HPOut4,
		"temp_HPOut5": temp_HPOut5,
		"temp_HPOut6": temp_HPOut6,
		"power": power, 
		"switch_log": switch_log,
		"rt": rt,
	}
	return data


def get_device_specs():
	######## Device Info ################
	flowmeter_info = FlowmeterInfo.objects.all()
	Inverter_info = InverterInfo.objects.all()
	watthourmeter_info = WattHourMeterInfo.objects.all()
	heatexchanger_info = HeatExchangerInfo.objects.all()
	heatpump_info = HeatPumpInfo.objects.all()
	circulatingpump_info = CirculatingPumpInfo.objects.all()
	deepwellpump_info = DeepwellPumpInfo.objects.all()
	data = {
		"flowmeter_info": flowmeter_info,
		"Inverter_info": Inverter_info,
		"watthourmeter_info": watthourmeter_info,
		"heatexchanger_info": heatexchanger_info,
		"heatpump_info": heatpump_info,
		"circulatingpump_info": circulatingpump_info,
		"deepwellpump_info": deepwellpump_info,
	}
	return data

def write_cmd(temp_mode, op_mode):
	if op_mode == 'AT':
		op_mode = '자동'

	# log.debug("op_mode: " + str(op_mode))
	####### create json file
	cp = CirculatingPumpLogger.objects.latest('id')
	dwp1 = DeepwellPump1Logger.objects.latest('id')
	dwp2 = DeepwellPump2Logger.objects.latest('id')
	dwp3 = DeepwellPump3Logger.objects.latest('id')
	dwp4 = DeepwellPump4Logger.objects.latest('id')
	rt = RefrigerationTonLogger.objects.latest('id')
	datetime = str(timezone.now())[:-7]
	cmd_text = {
		'temp_mode': temp_mode,
		'op_mode': op_mode,
		'cp': cp.switch,
		'cp_id': cp.CPID,
		'cp_hz': cp.Hz,
		'cp_flux': cp.flux,
		'dwp1': dwp1.switch,
		'dwp2': dwp2.switch,
		'dwp3': dwp3.switch,
		'dwp4': dwp4.switch,
		'datetime':datetime,
		'rt': rt.RT,
		'main': 'from_main'
	}
	# log.debug("cmd_text: " + str(cmd_text))
	with open(file_path + 'cmdmain.json', 'w') as fp:
		json.dump(cmd_text, fp)
	return 


def read_data_from_json(op_mode):
	data = {}
	try:
		with open(file_path + 'hmidata.json') as data_file:
			_data = json.load(data_file)

			datetime = _data["datetime"]
			op_mode = op_mode
			if op_mode == 'AT':
				op_mode = u'자동'

			data = {
				"heat_pump": [
					{
						"switch":_data["hp1"],
						"tempIn":_data["heo1"],
						"tempOut":_data["hpo1"],
					},
					{
						"switch":_data["hp2"],
						"tempIn":_data["heo1"],
						"tempOut":_data["hpo2"],
					},
					{
						"switch":_data["hp3"],
						"tempIn":_data["heo1"],
						"tempOut":_data["hpo3"],
					},
					{
						"switch":_data["hp4"],
						"tempIn":_data["heo1"],
						"tempOut":_data["hpo4"],
					},
					{
						"switch":_data["hp5"],
						"tempIn":_data["heo1"],
						"tempOut":_data["hpo5"],
					},
					{
						"switch":_data["hp6"],
						"tempIn":_data["heo1"],
						"tempOut":_data["hpo6"],
					}
				],
				"DWP": [
					{
						"switch":_data["dwp1"],
						"get_waterLevel_display":_data["dwp1_lv"],
					},
					{
						"switch":_data["dwp2"],
						"get_waterLevel_display":_data["dwp2_lv"],
					},
					{
						"switch":_data["dwp3"],
						"get_waterLevel_display":_data["dwp3_lv"],
					},
					{
						"switch":_data["dwp4"],
						"get_waterLevel_display":_data["dwp4_lv"],
					}
				],
				"circulating_pump": {
					"get_CPID_display":_data["cp_id"],
					"switch":_data["cp"],
					"Hz":_data["cp_hz"],
					"flux":_data["cp_flux"],
				},
				"DWPFM": {
					"temperature":_data["dwpfm_temp"],
					"currentFlux":_data["dwpfm_cur"],
					"integralFlux":_data["dwpfm_int"],
					"velocity":_data["dwpfm_vel"],
				},
				"CPFM": {
					"temperature":_data["cpfm_temp"],
					"currentFlux":_data["cpfm_cur"],
					"integralFlux":_data["cpfm_int"],
					"velocity":_data["cpfm_vel"],
				},

				"temp_HEIn1": {
					"temperature":_data["hei1"],
				},
				"temp_HEOut1": {
					"temperature": _data["heo1"],
				},
				"temp_HEIn2": {
					"temperature":_data["hei2"],
				},
				"temp_HEOut2": {
					"temperature":_data["heo2"],
				},
				"temp_HPIn1": _data["heo1"],
				"temp_HPIn2": _data["heo1"],
				"temp_HPIn3": _data["heo1"],
				"temp_HPIn4": _data["heo1"],
				"temp_HPIn5": _data["heo1"],
				"temp_HPIn6": _data["heo1"],
				"temp_HPOut1": _data["hpo1"],
				"temp_HPOut2": _data["hpo2"],
				"temp_HPOut3": _data["hpo3"],
				"temp_HPOut4": _data["hpo4"],
				"temp_HPOut5": _data["hpo5"],
				"temp_HPOut6": _data["hpo6"],
				"power": {
					"currentPowerConsumption":_data["pow_cur"],
				}, 
				"switch_log": {
					"dateTime":_data["datetime"],
				},
				"rt": {
					"RT":_data["rt"],
				},
				"op_mode": op_mode,
				"temp_mode":_data["temp_mode"],
			}


	except Exception, e:
		log.error(e)
		return False

	buf_a, buf_b, buf_c, buf_d = set_section_buffer()

	# 자동 모드인 경우 
	if op_mode == u"자동":	# op_mode가 unicode 형태이다. (unicode.encode('utf-8')하니까 한글 깨지더라)
		apply_rt_to_dwp(data)
		# log.debug("prev_section: " + prev_section)
		# log.debug("buf: " + str(buf_a) + ", " + str(buf_b) + ", " + str(buf_c) + ", " + str(buf_d))
		
		with open(file_path + 'dwp.json', 'r') as fp:
			dwp = json.load(fp)
		timenow = str(timezone.now())[:-7] #milisecond 제외

		# DWP 제어: 스위치 바뀌어야 하는 것만 바꾸고 db 저장
		# on으로 바뀌어야 하는 경우
		# 	dwp.json 에 dwp#: 0 으로 초기화
		# 	스위치 변경 및 db 저장 
		# off로 바뀌어야 하는 경우
		# 	dwp.json 에 dwp#: time 으로 저장
		# 	dwp.json 값이 이미 0이 아닌 시간이면 그냥 pass
		# 	후에 now-time > 5min 일 때 스위치 변경

		if _data["dwp1"] != data["DWP"][0]["switch"]:
			if data["DWP"][0]["switch"] == "ON": # OFF >> ON
				# on인 경우 off예정이었더라도 시간 삭제
				dwp.update({'dwp1': 0})
				
				dwp1 = DeepwellPump1Logger(
				    dateTime=datetime, opMode=op_mode, switch=data["DWP"][0]["switch"]
				    )
				new_cmd1 = OperationSwitchControl(
					dateTime=timezone.now(), location="DWP1", switch=data["DWP"][0]["switch"]
				)
				dwp1.save(); new_cmd1.save();
				write_cmd(data['temp_mode'], op_mode)
			else: # ON >> OFF
				# dwp.json 파일에 on으로 명시되었던 경우만 시간 적고
				if dwp["dwp1"] == 0:
					dwp.update({'dwp1':timenow})
				else: 
					check_off_delay1(str(dwp["dwp1"]), data)

		if _data["dwp2"] != data["DWP"][1]["switch"]:
			if data["DWP"][1]["switch"] == "ON": # OFF >> ON
				# on인 경우 off예정이었더라도 시간 삭제
				dwp.update({'dwp2': 0})
				
				dwp2 = DeepwellPump2Logger(
				    dateTime=datetime, opMode=op_mode, switch=data["DWP"][1]["switch"]
				    )
				new_cmd2 = OperationSwitchControl(
					dateTime=timezone.now(), location="DWP2", switch=data["DWP"][1]["switch"]
				)
				dwp2.save(); new_cmd2.save();
				write_cmd(data['temp_mode'], op_mode)
			else: # ON >> OFF
				if dwp["dwp2"] == 0:
					dwp.update({'dwp2':timenow})
				else: 
					check_off_delay2(str(dwp["dwp2"]), data)

		if _data["dwp3"] != data["DWP"][2]["switch"]:
			if data["DWP"][2]["switch"] == "ON": # OFF >> ON
				# on인 경우 off예정이었더라도 시간 삭제
				dwp.update({'dwp3': 0})
				
				dwp3 = DeepwellPump3Logger(
				    dateTime=datetime, opMode=op_mode, switch=data["DWP"][2]["switch"]
				    )
				new_cmd3 = OperationSwitchControl(
					dateTime=timezone.now(), location="DWP3", switch=data["DWP"][2]["switch"]
				)
				dwp3.save(); new_cmd3.save();
				write_cmd(data['temp_mode'], op_mode)
			else: # ON >> OFF
				if dwp["dwp3"] == 0:
					dwp.update({'dwp3':timenow})
				else: 
					check_off_delay3(str(dwp["dwp3"]), data)

		if _data["dwp4"] != data["DWP"][3]["switch"]:
			if data["DWP"][3]["switch"] == "ON": # OFF >> ON
				# on인 경우 off예정이었더라도 시간 삭제
				dwp.update({'dwp4': 0})
				
				dwp4 = DeepwellPump4Logger(
				    dateTime=datetime, opMode=op_mode, switch=data["DWP"][3]["switch"]
				    )
				new_cmd4 = OperationSwitchControl(
					dateTime=timezone.now(), location="DWP4", switch=data["DWP"][3]["switch"]
				)
				dwp4.save(); new_cmd4.save();
				write_cmd(data['temp_mode'], op_mode)
			else: # ON >> OFF
				if dwp["dwp4"] == 0:
					dwp.update({'dwp4':timenow})
				else: 
					check_off_delay4(str(dwp["dwp4"]), data)

		with open('dwp.json', 'w') as fp:
			 json.dump(dwp, fp)

		
		# log.debug("debug message!!!!!!!!!!!!!")
		# log.debug(off1 != "0")
		# log.debug(off4 != "0")
		# log.debug(type(off4))



		# end rt > dwp

		# 히트펌프에 따른 인버터(순환펌프) 출력 제어
		flux_need = 0
		if data["heat_pump"][0]["switch"] == "ON":
			flux_need = flux_need + 178
		if data["heat_pump"][1]["switch"] == "ON":
			flux_need = flux_need + 192
		if data["heat_pump"][2]["switch"] == "ON":
			flux_need = flux_need + 178
		if data["heat_pump"][3]["switch"] == "ON":
			flux_need = flux_need + 96
		if data["heat_pump"][4]["switch"] == "ON":
			flux_need = flux_need + 192
		if data["heat_pump"][5]["switch"] == "ON":
			flux_need = flux_need + 96
		flux_need = int(flux_need + flux_need*0.1)




		# maincmd.json command 전달
		# write_cmd(data['temp_mode'], op_mode)

	return data


def save_data():
	# hmidata.json 을 열어 안의 내용대로 DB에 저장
	try:
		with open(file_path + 'hmidata.json') as data_file:
			data = json.load(data_file)
			# log.error("!!!!!!!!!!!!!")

			datetime = data["datetime"]
			# log.error("" + datetime)
			datetime = dt.strptime(datetime, "%Y-%m-%d %H:%M:%S")
			# log.error("" + str(datetime))
			if(timezone.now() - datetime < timezone.timedelta(minutes=save_interval)):
				return
			log.error("minutes = " + str(save_interval))
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
				dateTime=datetime, CPID=data["cp_id"], opMode=op_mode, switch=data["cp"], Hz=data["cp_Hz"], flux=data["cp_flux"]
				)
			cp.save()

			dwpfm = DWPFlowmeterLogger(
			    dateTime=datetime, temperature=data["dwpfm_temp"], currentFlux=data["dwpfm_cur"], integralFlux=data["dwpfm_int"], velocity=data["dwpfm_vel"]
			    )
			cpfm = CPFlowmeterLogger(
			    dateTime=datetime, temperature=data["cpfm_temp"], currentFlux=data["cpfm_cur"], integralFlux=data["cpfm_int"], velocity=data["cpfm_vel"]
			    )
			dwpfm.save();cpfm.save();

			power = PowerConsumptionLogger(
			    dateTime=datetime, currentPowerConsumption=data["pow_cur"], integralPowerConsumption=data["pow_int"]
			    )
			power.save()
	except Exception, e:
		log.error(e)
		return False
	
	return True







def set_section_buffer():
	global prev_section
	global buf_a, buf_b, buf_c, buf_d

	# set buffer 
	if prev_section == 'a':
		buf_a = buf_b = buf_c = buf_d = 0
	elif prev_section == 'b':
		buf_a = pump_buffer
		buf_b = buf_c = buf_d = 0
	elif prev_section == 'c':
		buf_b = pump_buffer
		buf_a = buf_c = buf_d = 0
	elif prev_section == 'd':
		buf_c = pump_buffer
		buf_a = buf_b = buf_d = 0
	elif prev_section == 'e':
		buf_d = pump_buffer
		buf_a = buf_b = buf_c = 0

	return buf_a, buf_b, buf_c, buf_d

def apply_rt_to_dwp(data):
	global buf_a, buf_b, buf_c, buf_d
	# RT값에 따라 심정펌프 제어
	if data["temp_mode"] == u"냉방":
		if data["rt"]["RT"] < 20 - buf_a:
			data["DWP"][0]["switch"] = "OFF"
			data["DWP"][1]["switch"] = "ON"
			data["DWP"][2]["switch"] = "OFF"
			data["DWP"][3]["switch"] = "OFF"
			prev_section = 'a'
		elif data["rt"]["RT"] < 30 - buf_b:
			data["DWP"][0]["switch"] = "ON"
			data["DWP"][1]["switch"] = "OFF"
			data["DWP"][2]["switch"] = "OFF"
			data["DWP"][3]["switch"] = "OFF"
			prev_section = 'b'
		elif data["rt"]["RT"] < 50 - buf_c:
			data["DWP"][0]["switch"] = "ON"
			data["DWP"][1]["switch"] = "ON"
			data["DWP"][2]["switch"] = "OFF"
			data["DWP"][3]["switch"] = "OFF"
			prev_section = 'c'
		elif data["rt"]["RT"] < 70 - buf_d:
			data["DWP"][0]["switch"] = "ON"
			data["DWP"][1]["switch"] = "OFF"
			data["DWP"][2]["switch"] = "OFF"
			data["DWP"][3]["switch"] = "ON"
			prev_section = 'd'
		else:
			data["DWP"][0]["switch"] = "ON"
			data["DWP"][1]["switch"] = "ON"
			data["DWP"][2]["switch"] = "OFF"
			data["DWP"][3]["switch"] = "ON"
			prev_section = 'e'
	else:	# 난방 모드
		if data["rt"]["RT"] < 20 - buf_a:
			data["DWP"][0]["switch"] = "OFF"
			data["DWP"][1]["switch"] = "OFF"
			data["DWP"][2]["switch"] = "ON"
			data["DWP"][3]["switch"] = "OFF"
			prev_section = 'a'
		elif data["rt"]["RT"] < 30 - buf_b:
			data["DWP"][0]["switch"] = "ON"
			data["DWP"][1]["switch"] = "OFF"
			data["DWP"][2]["switch"] = "OFF"
			data["DWP"][3]["switch"] = "OFF"
			prev_section = 'b'
		elif data["rt"]["RT"] < 50 - buf_c:
			data["DWP"][0]["switch"] = "ON"
			data["DWP"][1]["switch"] = "OFF"
			data["DWP"][2]["switch"] = "ON"
			data["DWP"][3]["switch"] = "OFF"
			prev_section = 'c'
		elif data["rt"]["RT"] < 70 - buf_d:
			data["DWP"][0]["switch"] = "ON"
			data["DWP"][1]["switch"] = "OFF"
			data["DWP"][2]["switch"] = "OFF"
			data["DWP"][3]["switch"] = "ON"
			prev_section = 'd'
		else:
			data["DWP"][0]["switch"] = "ON"
			data["DWP"][1]["switch"] = "OFF"
			data["DWP"][2]["switch"] = "ON"
			data["DWP"][3]["switch"] = "ON"
			prev_section = 'e'



def check_off_delay1(off1, data):
	if off1 != "0":
		offtime = dt.strptime(off1, "%Y-%m-%d %H:%M:%S")
		if(timezone.now() - offtime > timezone.timedelta(minutes=pump_off_delay)):
			dwp = DeepwellPump1Logger(
			    dateTime=datetime, opMode=op_mode, switch="OFF"
			    )
			new_cmd = OperationSwitchControl(
				dateTime=timezone.now(), location="DWP1", switch="OFF"
			)
			dwp.save(); new_cmd.save();
			write_cmd(data['temp_mode'], data['op_mode'])
		else :	# 5분이 아직 안지났으면 상태는 on
			data["DWP"][0]["switch"] = "ON"

def check_off_delay2(off2, data):
	if off2 != "0":
		offtime = dt.strptime(off2, "%Y-%m-%d %H:%M:%S")
		if(timezone.now() - offtime > timezone.timedelta(minutes=5)):
			dwp = DeepwellPump2Logger(
			    dateTime=datetime, opMode=op_mode, switch="ON"
			    )
			new_cmd = OperationSwitchControl(
				dateTime=timezone.now(), location="DWP2", switch="OFF"
			)
			dwp.save(); new_cmd.save();
			write_cmd(data['temp_mode'], data['op_mode'])
		else :	# 5분이 아직 안지났으면 상태는 on
			data["DWP"][1]["switch"] = "ON"

def check_off_delay3(off3, data):
	if off3 != "0":
		offtime = dt.strptime(off3, "%Y-%m-%d %H:%M:%S")
		if(timezone.now() - offtime > timezone.timedelta(minutes=5)):
			dwp = DeepwellPump3Logger(
			    dateTime=datetime, opMode=op_mode, switch="ON"
			    )
			new_cmd = OperationSwitchControl(
				dateTime=timezone.now(), location="DWP3", switch="OFF"
			)
			dwp.save(); new_cmd.save();
			write_cmd(data['temp_mode'], data['op_mode'])
		else :	# 5분이 아직 안지났으면 상태는 on
			data["DWP"][2]["switch"] = "ON"

def check_off_delay4(off4, data):
	if off4 != "0":
		offtime = dt.strptime(off4, "%Y-%m-%d %H:%M:%S")
		if(timezone.now() - offtime > timezone.timedelta(minutes=5)):
			dwp = DeepwellPump4Logger(
			    dateTime=datetime, opMode=op_mode, switch="ON"
			    )
			new_cmd = OperationSwitchControl(
				dateTime=timezone.now(), location="DWP4", switch="OFF"
			)
			dwp.save(); new_cmd.save();
			write_cmd(data['temp_mode'], data['op_mode'])
		else :	# 5분이 아직 안지났으면 상태는 on
			data["DWP"][3]["switch"] = "ON"
