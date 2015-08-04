#-*- coding: utf-8 -*-
from .models import *

from django.core.paginator import Paginator, EmptyPage
from django.utils import timezone
import simplejson as json
from datetime import datetime as dt

import logging
log = logging.getLogger(__name__)

import os, myproject.settings
file_path = os.path.join(myproject.settings.BASE_DIR, 'share/')

# rt값 다운될 때 버퍼 (껏다켰다 반복되지 않게)
# a~e, rt 구분에 따른 5구간
prev_section = 'a' 	
# rt 다운될 때 구간별 버퍼
buf_a = 0; buf_b = 0; buf_c = 0; buf_d = 0;	
# rt값 다운될 때 완충값 (껏다켰다 반복되지 않게)
pump_buffer = 2 		

# 심정펌프가 꺼질 때 다른 펌프가 풀가동 될 때까지 기다렸다 꺼짐
pump_off_delay = 30 # seconds


def get_operation_log(page):
	# 기기 동작 내역
	logs_per_page = 10
	page_no = 5

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
	# hmi에 주는 명령
	# if op_mode == 'AT':
	# 	op_mode = '자동'
	# else:
	# 	op_mode = '수동'
	# if temp_mode == 'CL':
	# 	temp_mode = '냉방'
	# else:
	# 	temp_mode = '난방'

	####### create json file
	cp = CirculatingPumpLogger.objects.latest('id')
	dwp1 = DeepwellPump1Logger.objects.latest('id')
	dwp2 = DeepwellPump2Logger.objects.latest('id')
	dwp3 = DeepwellPump3Logger.objects.latest('id')
	dwp4 = DeepwellPump4Logger.objects.latest('id')
	rt = RefrigerationTonLogger.objects.latest('id')
	datetime = str(timezone.now())[:-7]
	if cp.switch == "OFF":
		cp.Hz = 0
		cp.flux = 0
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
	log.debug(cmd_text)
	with open(file_path + 'cmdmain.json', 'w') as fp:
		json.dump(cmd_text, fp)
	return 


def read_data_from_json(op_mode):
	# hmi에서 데이터 읽어 옴
	data = {}
	try:
		with open(file_path + 'hmidata.json') as data_file:
			_data = json.load(data_file)

	except Exception, e:
		log.error(e)
		return { "error": e }

	datetime = _data["datetime"]
	op_mode = op_mode
	temp_mode = "CL"

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
			"integralPowerConsumption":_data["pow_int"],
		}, 
		"dateTime":_data["datetime"],
		"rt": {
			"RT":_data["rt"],
		},
		"op_mode": op_mode,
		"temp_mode": temp_mode,
	}

	buf_a, buf_b, buf_c, buf_d = set_section_buffer()

	# 자동 모드인 경우 
	if op_mode == 'AT':	



		# 히트펌프에 따른 인버터(순환펌프) 출력 제어
		flux_need = 0
		if data["heat_pump"][0]["switch"] == "ON":
			flux_need = flux_need + 178
			data["rt"]["RT"] = 90
			rt = RefrigerationTonLogger(
				dateTime=timezone.now(), RT=data["rt"]["RT"]
				).save()
			data["circulating_pump"]["switch"] = "ON"
		if data["heat_pump"][1]["switch"] == "ON":
			flux_need = flux_need + 192
			data["rt"]["RT"] = 90
			rt = RefrigerationTonLogger(
				dateTime=timezone.now(), RT=data["rt"]["RT"]
				).save()
			data["circulating_pump"]["switch"] = "ON"
		if data["heat_pump"][2]["switch"] == "ON":
			flux_need = flux_need + 178
			data["rt"]["RT"] = 90
			rt = RefrigerationTonLogger(
				dateTime=timezone.now(), RT=data["rt"]["RT"]
				).save()
			data["circulating_pump"]["switch"] = "ON"
		if data["heat_pump"][3]["switch"] == "ON":
			flux_need = flux_need + 96
			data["rt"]["RT"] = 90
			rt = RefrigerationTonLogger(
				dateTime=timezone.now(), RT=data["rt"]["RT"]
				).save()
			data["circulating_pump"]["switch"] = "ON"
		if data["heat_pump"][4]["switch"] == "ON":
			flux_need = flux_need + 192
			data["rt"]["RT"] = 90
			rt = RefrigerationTonLogger(
				dateTime=timezone.now(), RT=data["rt"]["RT"]
				).save()
			data["circulating_pump"]["switch"] = "ON"
		if data["heat_pump"][5]["switch"] == "ON":
			flux_need = flux_need + 96
			data["rt"]["RT"] = 90
			rt = RefrigerationTonLogger(
				dateTime=timezone.now(), RT=data["rt"]["RT"]
				).save()
			data["circulating_pump"]["switch"] = "ON"

		# flux_need = int(flux_need + flux_need*0.1)
		# if data["circulating_pump"]["flux"] != flux_need:
			# 60 : 1000

		if data["heat_pump"][0]["switch"] == "OFF" and data["heat_pump"][1]["switch"] == "OFF" and data["heat_pump"][2]["switch"] == "OFF" and data["heat_pump"][3]["switch"] == "OFF" and data["heat_pump"][4]["switch"] == "OFF" and data["heat_pump"][5]["switch"] == "OFF" :
			data["rt"]["RT"] = 0
			rt = RefrigerationTonLogger(
				dateTime=timezone.now(), RT=data["rt"]["RT"]
				).save()

			if data["circulating_pump"]["switch"] != "OFF":
				data["circulating_pump"]["switch"] = "OFF"
				data["circulating_pump"]["Hz"] = 0
				data["circulating_pump"]["flux"] = 0
				cp = CirculatingPumpLogger(
					dateTime=timezone.now(), 
					CPID=data["circulating_pump"]["get_CPID_display"], 
					opMode=op_mode, 
					switch="OFF", 
					Hz=0, 
					flux=0
					).save()
				new_cmd = OperationSwitchControl(
						dateTime=timezone.now(), location="CP"+str(data["circulating_pump"]["get_CPID_display"]), switch="OFF"
					).save()
				write_cmd(temp_mode, op_mode)


		if data["circulating_pump"]["switch"] == "ON" and data["circulating_pump"]["Hz"] != 60:
			cp = CirculatingPumpLogger(
				dateTime=timezone.now(), 
				CPID=data["circulating_pump"]["get_CPID_display"], 
				opMode=op_mode, 
				switch=data["circulating_pump"]["switch"], 
				Hz=60, 
				flux=data["circulating_pump"]["flux"]
				).save()
			new_cmd = OperationSwitchControl(
					dateTime=timezone.now(), location="CP"+str(data["circulating_pump"]["get_CPID_display"]), switch="ON"
				).save()
			write_cmd(temp_mode, op_mode)

		# end of 히트펌프 on시 rt 변경
		apply_rt_to_dwp(data)
		
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
				# command가 on인 경우 off 예정이었더라도 시간 삭제
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
				# dwp.json 파일에 on으로 명시되어있었던 경우만 시간 적음
				if dwp["dwp1"] == 0:
					dwp.update({'dwp1':timenow})
					# data["DWP"][0]["switch"] = "ON"
				else: 
					check_off_delay1(dwp, data)

		if _data["dwp2"] != data["DWP"][1]["switch"]:
			if data["DWP"][1]["switch"] == "ON": # OFF >> ON
				# command가 on인 경우 off 예정이었더라도 시간 삭제
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
			# dwp.json 파일에 on으로 명시되어있었던 경우만 시간 적음
				if dwp["dwp2"] == 0:
					dwp.update({'dwp2':timenow})
					# data["DWP"][1]["switch"] = "ON"
				else: 
					check_off_delay2(dwp, data)

		if _data["dwp3"] != data["DWP"][2]["switch"]:
			if data["DWP"][2]["switch"] == "ON": # OFF >> ON
				# command가 on인 경우 off 예정이었더라도 시간 삭제
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
			# dwp.json 파일에 on으로 명시되어있었던 경우만 시간 적음
				if dwp["dwp3"] == 0:
					dwp.update({'dwp3':timenow})
					# data["DWP"][2]["switch"] = "ON"
				else: 
					check_off_delay3(dwp, data)

		if _data["dwp4"] != data["DWP"][3]["switch"]:
			if data["DWP"][3]["switch"] == "ON": # OFF >> ON
				# command가 on인 경우 off 예정이었더라도 시간 삭제
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
			# dwp.json 파일에 on으로 명시되어있었던 경우만 시간 적음
				if dwp["dwp4"] == 0:
					dwp.update({'dwp4':timenow})
					# data["DWP"][3]["switch"] = "ON"
				else: 
					check_off_delay4(dwp, data)

		with open(file_path + 'dwp.json', 'w') as fp:
			 json.dump(dwp, fp)

		# end: rt 에 따른 dwp 제어

		# cmd가 바뀔 때마다 (새로운 DB를 저장할 때) cmdmain.json command 전달
		

	return data



def set_section_buffer():
	# rt값 다운될 때 버퍼 적용 구간 설정
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
	if data["temp_mode"] == 'CL': # 냉방 모드
		if data["rt"]["RT"] == 0:
			data["DWP"][0]["switch"] = "OFF"
			data["DWP"][1]["switch"] = "OFF"
			data["DWP"][2]["switch"] = "OFF"
			data["DWP"][3]["switch"] = "OFF"
		elif data["rt"]["RT"] < 20 - buf_a:
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
		if data["rt"]["RT"] == 0:
			data["DWP"][0]["switch"] = "OFF"
			data["DWP"][1]["switch"] = "OFF"
			data["DWP"][2]["switch"] = "OFF"
			data["DWP"][3]["switch"] = "OFF"
		elif data["rt"]["RT"] < 20 - buf_a:
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


# 심정펌프 전원 off시 delay
def check_off_delay1(dwp, data):
	off1 = str(dwp["dwp1"])
	if off1 != "0":
		offtime = dt.strptime(off1, "%Y-%m-%d %H:%M:%S")
		if (timezone.now() - offtime) > timezone.timedelta(seconds=pump_off_delay):
			dwp1 = DeepwellPump1Logger(
			    dateTime=timezone.now(), opMode=data["op_mode"], switch="OFF"
			    )
			new_cmd = OperationSwitchControl(
				dateTime=timezone.now(), location="DWP1", switch="OFF"
			)
			dwp1.save(); new_cmd.save();
			write_cmd(data['temp_mode'], data['op_mode'])
			# dwp["dwp1"] = 0
		else :	# 5분이 아직 안지났으면 상태는 on
			data["DWP"][0]["switch"] = "ON"

def check_off_delay2(dwp, data):
	off2 = str(dwp["dwp2"])
	# log.debug("off2: " + off2)
	if off2 != "0":
		offtime = dt.strptime(off2, "%Y-%m-%d %H:%M:%S")
		if(timezone.now() - offtime > timezone.timedelta(seconds=(pump_off_delay+1))):
			# log.debug(timezone.now() - offtime)
			dwp2 = DeepwellPump2Logger(
			    dateTime=timezone.now(), opMode=data["op_mode"], switch="OFF"
			    )
			new_cmd = OperationSwitchControl(
				dateTime=timezone.now(), location="DWP2", switch="OFF"
			)
			dwp2.save(); new_cmd.save();
			write_cmd(data['temp_mode'], data['op_mode'])
			# dwp["dwp2"] = 0
		else :	# 5분이 아직 안지났으면 상태는 on
			data["DWP"][1]["switch"] = "ON"

def check_off_delay3(dwp, data):
	off3 = str(dwp["dwp3"])
	if off3 != "0":
		offtime = dt.strptime(off3, "%Y-%m-%d %H:%M:%S")
		if(timezone.now() - offtime > timezone.timedelta(seconds=(pump_off_delay+2))):
			dwp3 = DeepwellPump3Logger(
			    dateTime=timezone.now(), opMode=data["op_mode"], switch="OFF"
			    )
			new_cmd = OperationSwitchControl(
				dateTime=timezone.now(), location="DWP3", switch="OFF"
			)
			dwp3.save(); new_cmd.save();
			write_cmd(data['temp_mode'], data['op_mode'])
			# dwp["dwp3"] = 0
		else :	# 5분이 아직 안지났으면 상태는 on
			data["DWP"][2]["switch"] = "ON"

def check_off_delay4(dwp, data):
	off4 = str(dwp["dwp4"])
	if off4 != "0":
		offtime = dt.strptime(off4, "%Y-%m-%d %H:%M:%S")
		if(timezone.now() - offtime > timezone.timedelta(seconds=(pump_off_delay+3))):
			dwp4 = DeepwellPump4Logger(
			    dateTime=timezone.now(), opMode=data["op_mode"], switch="OFF"
			    )
			new_cmd = OperationSwitchControl(
				dateTime=timezone.now(), location="DWP4", switch="OFF"
			)
			dwp4.save(); new_cmd.save();
			write_cmd(data['temp_mode'], data['op_mode'])
			# dwp["dwp4"] = 0
		else :	# 5분이 아직 안지났으면 상태는 on
			data["DWP"][3]["switch"] = "ON"



def save_data(data):
	# hmidata (+자동 제어 보정) 내용대로 DB에 저장
	op_mode = data["op_mode"]

	###### save models
	# HE temperature
	hei1 = TempHEIn1Logger(dateTime=timezone.now(),temperature=data["temp_HEIn1"]["temperature"])
	heo1 = TempHEOut1Logger(dateTime=timezone.now(),temperature=data["temp_HEOut1"]["temperature"])
	hei2 = TempHEIn2Logger(dateTime=timezone.now(),temperature=data["temp_HEIn2"]["temperature"])
	heo2 = TempHEOut2Logger(dateTime=timezone.now(),temperature=data["temp_HEOut2"]["temperature"])
	hei1.save(); hei2.save(); heo1.save(); heo1.save();

	# HP in temperature
	hpi1 = TempHPIn1Logger(dateTime=timezone.now(),temperature=data["temp_HPIn1"])
	hpi2 = TempHPIn2Logger(dateTime=timezone.now(),temperature=data["temp_HPIn2"])
	hpi3 = TempHPIn3Logger(dateTime=timezone.now(),temperature=data["temp_HPIn3"])
	hpi4 = TempHPIn4Logger(dateTime=timezone.now(),temperature=data["temp_HPIn4"])
	hpi5 = TempHPIn5Logger(dateTime=timezone.now(),temperature=data["temp_HPIn5"])
	hpi6 = TempHPIn6Logger(dateTime=timezone.now(),temperature=data["temp_HPIn6"])
	hpi1.save();hpi2.save();hpi3.save();hpi4.save();hpi5.save();hpi6.save();

	# HP out temperature
	hpo1 = TempHPOut1Logger(dateTime=timezone.now(),temperature=data["temp_HPOut1"])
	hpo2 = TempHPOut2Logger(dateTime=timezone.now(),temperature=data["temp_HPOut2"])
	hpo3 = TempHPOut3Logger(dateTime=timezone.now(),temperature=data["temp_HPOut3"])
	hpo4 = TempHPOut4Logger(dateTime=timezone.now(),temperature=data["temp_HPOut4"])
	hpo5 = TempHPOut5Logger(dateTime=timezone.now(),temperature=data["temp_HPOut5"])
	hpo6 = TempHPOut6Logger(dateTime=timezone.now(),temperature=data["temp_HPOut6"])
	hpo1.save();hpo2.save();hpo3.save();hpo4.save();hpo5.save();hpo6.save();

	# Heat pump
	hp1 = HeatPump1Logger(
	    dateTime=timezone.now(), opMode=op_mode, switch=data["heat_pump"][0]["switch"], 
	    tempIn=hpi1, tempOut=hpo1
	    )
	hp2 = HeatPump2Logger(
	    dateTime=timezone.now(), opMode=op_mode, switch=data["heat_pump"][1]["switch"], 
	    tempIn=hpi2, tempOut=hpo2
	    )
	hp3 = HeatPump3Logger(
	    dateTime=timezone.now(), opMode=op_mode, switch=data["heat_pump"][2]["switch"], 
	    tempIn=hpi3, tempOut=hpo3
	    )
    	hp4 = HeatPump4Logger(
	    dateTime=timezone.now(), opMode=op_mode, switch=data["heat_pump"][3]["switch"], 
	    tempIn=hpi4, tempOut=hpo4
	    )
	hp5 = HeatPump5Logger(
	    dateTime=timezone.now(), opMode=op_mode, switch=data["heat_pump"][4]["switch"], 
	    tempIn=hpi5, tempOut=hpo5
	    )
	hp6 = HeatPump6Logger(
	    dateTime=timezone.now(), opMode=op_mode, switch=data["heat_pump"][5]["switch"], 
	    tempIn=hpi6, tempOut=hpo6
	    )
	hp1.save();hp2.save();hp3.save();hp4.save();hp5.save();hp6.save()

	# Deep well pump
	dwp1 = DeepwellPump1Logger(
	    dateTime=timezone.now(), opMode=op_mode, 
	    switch=data["DWP"][0]["switch"],
	    waterLevel=data["DWP"][0]["get_waterLevel_display"]
	    )
	dwp2 = DeepwellPump2Logger(
	    dateTime=timezone.now(), opMode=op_mode, 
	    switch=data["DWP"][1]["switch"],
	    waterLevel=data["DWP"][1]["get_waterLevel_display"]
	    )
	dwp3 = DeepwellPump3Logger(
	    dateTime=timezone.now(), opMode=op_mode, 
	    switch=data["DWP"][2]["switch"],
	    waterLevel=data["DWP"][2]["get_waterLevel_display"]
	    )
	dwp4 = DeepwellPump4Logger(
	    dateTime=timezone.now(), opMode=op_mode, 
	    switch=data["DWP"][3]["switch"],
	    waterLevel=data["DWP"][3]["get_waterLevel_display"]
	    )
	dwp1.save();dwp2.save();dwp3.save();dwp4.save();

	cp = CirculatingPumpLogger(
		dateTime=timezone.now(), 
		CPID=data["circulating_pump"]["get_CPID_display"], 
		opMode=op_mode, 
		switch=data["circulating_pump"]["switch"], 
		Hz=data["circulating_pump"]["Hz"], 
		flux=data["circulating_pump"]["flux"]
		)
	cp.save()

	dwpfm = DWPFlowmeterLogger(
		dateTime=timezone.now(), 
		temperature=data["DWPFM"]["temperature"], 
		currentFlux=data["DWPFM"]["currentFlux"], 
		integralFlux=data["DWPFM"]["integralFlux"],
		velocity=data["DWPFM"]["velocity"]
		)
	dwpfm.save()
	cpfm = CPFlowmeterLogger(
    		dateTime=timezone.now(), 
		temperature=data["CPFM"]["temperature"], 
		currentFlux=data["CPFM"]["currentFlux"], 
		integralFlux=data["CPFM"]["integralFlux"],
		velocity=data["CPFM"]["velocity"]
		)
	cpfm.save()

	power = PowerConsumptionLogger(
		dateTime=timezone.now(), 
		currentPowerConsumption=data["power"]["currentPowerConsumption"], 
		integralPowerConsumption=data["power"]["integralPowerConsumption"]
		)
	power.save()

	rt = RefrigerationTonLogger(
		dateTime=timezone.now(), RT=data["rt"]["RT"]
		)
	rt.save()
	
	return True


def set_cp(id, opMode, switch, hz, flux):
	# 인버터 설정
	cp = CirculatingPumpLogger(
		dateTime=timezone.now(), CPID=id, opMode=opMode, switch=switch, Hz=hz, flux=flux
		).save()
	new_cmd = OperationSwitchControl(
			dateTime=timezone.now(), location="CP"+str(id), switch=switch
		).save()
	return


def get_CIU_from_json(floor):
	ciu_dict = {}
	file1 = file_path +'ciu1.json'
	file2 = file_path +'ciu2.json'
	file3 = file_path +'ciu3.json'
	count = 0

	# log.debug("floor: " + str(floor) + ", type: " + str(type(floor)))

	# 실내기 정보 파일에서 읽어옴
	# 1층
	with open(file1, 'r') as data_file:
		data = json.load(data_file)
		if floor == "1":
			ciu_dict = data
		for ciu in data["us"]:
			if ciu["switch"] == "ON":
				count = count+1
	
	# 2층
	with open(file2, 'r') as data_file:
		data = json.load(data_file)
		if floor == "2":
			ciu_dict = data
		for ciu in data["us"]:
			if ciu["switch"] == "ON":
				count = count+1
	
	# 3층
	with open(file3, 'r') as data_file:
		data = json.load(data_file)
		if floor == "3":
			ciu_dict = data
		for ciu in data["us"]:
			if ciu["switch"] == "ON":
				count = count+1

	ciu_dict.update({"ciu_on_count": count})
	return ciu_dict


def get_CIU_on_HP(no):
	if no == "1":
		ret = CiuOnHeatPump1.objects.latest('id')
	elif no == "2":
		ret = CiuOnHeatPump2.objects.latest('id')
	elif no == "3":
		ret = CiuOnHeatPump3.objects.latest('id')
	elif no == "4":
		ret = CiuOnHeatPump4.objects.latest('id')
	elif no == "5":
		ret = CiuOnHeatPump5.objects.latest('id')
	else: # no == 6
		ret = CiuOnHeatPump6.objects.latest('id')

	# log.debug(str(ret.to_dict()))
	# ciu_dict = ret.to_dict()
	return {"ciu_on_hp": ret.items()}


def get_CIU_on_HP_from_json(no):
	ciu_on_hp = []
	file1 = file_path +'ciu1.json'
	file2 = file_path +'ciu2.json'
	file3 = file_path +'ciu3.json'
	
	# ciu1.json
	if no == "5":
		with open(file1, 'r') as data_file:
			data = json.load(data_file)
		ciu_on_hp = data["us"][5:14]
	# ciu2.json
	elif no == "2":
		with open(file2, 'r') as data_file:
			data = json.load(data_file)
		ciu_on_hp = data["us"][7:12]
	elif no == "3":
		with open(file2, 'r') as data_file:
			data = json.load(data_file)
		ciu_on_hp = data["us"][1:7]

	# ciu3.json
	elif no == "1":
		with open(file3, 'r') as data_file:
			data = json.load(data_file)
		ciu_on_hp = data["us"][8:12]
	elif no == "6":
		with open(file3, 'r') as data_file:
			data = json.load(data_file)
		ciu_on_hp = data["us"][1:8]
		
	# ciu1+2+3
	else: # no == 4
		with open(file1, 'r') as data_file:
			data = json.load(data_file)
		ciu_on_hp = data["us"][:5]
		with open(file2, 'r') as data_file:
			data = json.load(data_file)
		ciu_on_hp.append(data["us"][0])
		with open(file3, 'r') as data_file:
			data = json.load(data_file)
		ciu_on_hp.append(data["us"][0])

	return {"ciu_on_hp": ciu_on_hp}


def get_CIU(floor):
	# 실내기 정보 db에서 읽어옴
	if floor == 1:
		us = Floor1CIUs.objects.latest('id')

		data = {
			"us": [
				{ 
					"switch":us.u1.switch,
					"temperature":us.u1.temperature,
					"set_temp":us.u1.setTemp,
					"op_mode":us.u1.get_opMode_display,
					"air_flow":us.u1.get_airFlow_display,
					"state":us.u1.get_state_display,
				},
				{ 
					"switch":us.u2.switch,
					"temperature":us.u2.temperature,
					"set_temp":us.u2.setTemp,
					"op_mode":us.u2.get_opMode_display,
					"air_flow":us.u2.get_airFlow_display,
					"state":us.u2.get_state_display,
				},
				{ 
					"switch":us.u3.switch,
					"temperature":us.u3.temperature,
					"set_temp":us.u3.setTemp,
					"op_mode":us.u3.get_opMode_display,
					"air_flow":us.u3.get_airFlow_display,
					"state":us.u3.get_state_display,
				},
				{ 
					"switch":us.u4.switch,
					"temperature":us.u4.temperature,
					"set_temp":us.u4.setTemp,
					"op_mode":us.u4.get_opMode_display,
					"air_flow":us.u4.get_airFlow_display,
					"state":us.u4.get_state_display,
				},
				{ 
					"switch":us.u5.switch,
					"temperature":us.u5.temperature,
					"set_temp":us.u5.setTemp,
					"op_mode":us.u5.get_opMode_display,
					"air_flow":us.u5.get_airFlow_display,
					"state":us.u5.get_state_display,
				},
				{ 
					"switch":us.u6.switch,
					"temperature":us.u6.temperature,
					"set_temp":us.u6.setTemp,
					"op_mode":us.u6.get_opMode_display,
					"air_flow":us.u6.get_airFlow_display,
					"state":us.u6.get_state_display,
				},
				{ 
					"switch":us.u7.switch,
					"temperature":us.u7.temperature,
					"set_temp":us.u7.setTemp,
					"op_mode":us.u7.get_opMode_display,
					"air_flow":us.u7.get_airFlow_display,
					"state":us.u7.get_state_display,
				},
				{ 
					"switch":us.u8.switch,
					"temperature":us.u8.temperature,
					"set_temp":us.u8.setTemp,
					"op_mode":us.u8.get_opMode_display,
					"air_flow":us.u8.get_airFlow_display,
					"state":us.u8.get_state_display,
				},
				{ 
					"switch":us.u9.switch,
					"temperature":us.u9.temperature,
					"set_temp":us.u9.setTemp,
					"op_mode":us.u9.get_opMode_display,
					"air_flow":us.u9.get_airFlow_display,
					"state":us.u9.get_state_display,
				},
				{ 
					"switch":us.u10.switch,
					"temperature":us.u10.temperature,
					"set_temp":us.u10.setTemp,
					"op_mode":us.u10.get_opMode_display,
					"air_flow":us.u10.get_airFlow_display,
					"state":us.u10.get_state_display,
				},
				{ 
					"switch":us.u11.switch,
					"temperature":us.u11.temperature,
					"set_temp":us.u11.setTemp,
					"op_mode":us.u11.get_opMode_display,
					"air_flow":us.u11.get_airFlow_display,
					"state":us.u11.get_state_display,
				},
				{ 
					"switch":us.u12.switch,
					"temperature":us.u12.temperature,
					"set_temp":us.u12.setTemp,
					"op_mode":us.u12.get_opMode_display,
					"air_flow":us.u12.get_airFlow_display,
					"state":us.u12.get_state_display,
				},
				{ 
					"switch":us.u13.switch,
					"temperature":us.u13.temperature,
					"set_temp":us.u13.setTemp,
					"op_mode":us.u13.get_opMode_display,
					"air_flow":us.u13.get_airFlow_display,
					"state":us.u13.get_state_display,
				},
				{ 
					"switch":us.u14.switch,
					"temperature":us.u14.temperature,
					"set_temp":us.u14.setTemp,
					"op_mode":us.u14.get_opMode_display,
					"air_flow":us.u14.get_airFlow_display,
					"state":us.u14.get_state_display,
				}
			]
		}
		return data

	elif floor == 2:
		us= Floor2CIUs.objects.latest('id')
	else: 
		us = Floor3CIUs.objects.latest('id')
	
	data = {
		"us": [
			{ 
				"switch":us.u1.switch,
				"temperature":us.u1.temperature,
				"set_temp":us.u1.setTemp,
				"op_mode":us.u1.get_opMode_display,
				"air_flow":us.u1.get_airFlow_display,
				"state":us.u1.get_state_display,
			},
			{ 
				"switch":us.u2.switch,
				"temperature":us.u2.temperature,
				"set_temp":us.u2.setTemp,
				"op_mode":us.u2.get_opMode_display,
				"air_flow":us.u2.get_airFlow_display,
				"state":us.u2.get_state_display,
			},
			{ 
				"switch":us.u3.switch,
				"temperature":us.u3.temperature,
				"set_temp":us.u3.setTemp,
				"op_mode":us.u3.get_opMode_display,
				"air_flow":us.u3.get_airFlow_display,
				"state":us.u3.get_state_display,
			},
			{ 
				"switch":us.u4.switch,
				"temperature":us.u4.temperature,
				"set_temp":us.u4.setTemp,
				"op_mode":us.u4.get_opMode_display,
				"air_flow":us.u4.get_airFlow_display,
				"state":us.u4.get_state_display,
			},
			{ 
				"switch":us.u5.switch,
				"temperature":us.u5.temperature,
				"set_temp":us.u5.setTemp,
				"op_mode":us.u5.get_opMode_display,
				"air_flow":us.u5.get_airFlow_display,
				"state":us.u5.get_state_display,
			},
			{ 
				"switch":us.u6.switch,
				"temperature":us.u6.temperature,
				"set_temp":us.u6.setTemp,
				"op_mode":us.u6.get_opMode_display,
				"air_flow":us.u6.get_airFlow_display,
				"state":us.u6.get_state_display,
			},
			{ 
				"switch":us.u7.switch,
				"temperature":us.u7.temperature,
				"set_temp":us.u7.setTemp,
				"op_mode":us.u7.get_opMode_display,
				"air_flow":us.u7.get_airFlow_display,
				"state":us.u7.get_state_display,
			},
			{ 
				"switch":us.u8.switch,
				"temperature":us.u8.temperature,
				"set_temp":us.u8.setTemp,
				"op_mode":us.u8.get_opMode_display,
				"air_flow":us.u8.get_airFlow_display,
				"state":us.u8.get_state_display,
			},
			{ 
				"switch":us.u9.switch,
				"temperature":us.u9.temperature,
				"set_temp":us.u9.setTemp,
				"op_mode":us.u9.get_opMode_display,
				"air_flow":us.u9.get_airFlow_display,
				"state":us.u9.get_state_display,
			},
			{ 
				"switch":us.u10.switch,
				"temperature":us.u10.temperature,
				"set_temp":us.u10.setTemp,
				"op_mode":us.u10.get_opMode_display,
				"air_flow":us.u10.get_airFlow_display,
				"state":us.u10.get_state_display,
			},
			{ 
				"switch":us.u11.switch,
				"temperature":us.u11.temperature,
				"set_temp":us.u11.setTemp,
				"op_mode":us.u11.get_opMode_display,
				"air_flow":us.u11.get_airFlow_display,
				"state":us.u11.get_state_display,
			},
			{ 
				"switch":us.u12.switch,
				"temperature":us.u12.temperature,
				"set_temp":us.u12.setTemp,
				"op_mode":us.u12.get_opMode_display,
				"air_flow":us.u12.get_airFlow_display,
				"state":us.u12.get_state_display,
			}
		]
	}
	return data

def save_ciu1(data):
	f1 = [None]*14
	f1[0] = Floor1CIU1(
		dateTime=timezone.now(), switch=data["us"][0]["switch"],temperature=data["us"][0]["temperature"], setTemp=data["us"][0]["set_temp"],
		opMode=data["us"][0]["op_mode"],airFlow=data["us"][0]["air_flow"],state=data["us"][0]["state"],
		)
	f1[1] = Floor1CIU2(
		dateTime=timezone.now(), switch=data["us"][1]["switch"],temperature=data["us"][1]["temperature"], setTemp=data["us"][1]["set_temp"],
		opMode=data["us"][1]["op_mode"],airFlow=data["us"][1]["air_flow"],state=data["us"][1]["state"],
		)
	f1[2] = Floor1CIU3(
		dateTime=timezone.now(), switch=data["us"][2]["switch"],temperature=data["us"][2]["temperature"], setTemp=data["us"][2]["set_temp"],
		opMode=data["us"][2]["op_mode"],airFlow=data["us"][2]["air_flow"],state=data["us"][2]["state"],
		)
	f1[3] = Floor1CIU4(
		dateTime=timezone.now(), switch=data["us"][3]["switch"],temperature=data["us"][3]["temperature"], setTemp=data["us"][3]["set_temp"],
		opMode=data["us"][3]["op_mode"],airFlow=data["us"][3]["air_flow"],state=data["us"][3]["state"],
		)
	f1[4] = Floor1CIU5(
		dateTime=timezone.now(), switch=data["us"][4]["switch"],temperature=data["us"][4]["temperature"], setTemp=data["us"][4]["set_temp"],
		opMode=data["us"][4]["op_mode"],airFlow=data["us"][4]["air_flow"],state=data["us"][4]["state"],
		)
	f1[5] = Floor1CIU6(
		dateTime=timezone.now(), switch=data["us"][5]["switch"],temperature=data["us"][5]["temperature"], setTemp=data["us"][5]["set_temp"],
		opMode=data["us"][5]["op_mode"],airFlow=data["us"][5]["air_flow"],state=data["us"][5]["state"],
		)
	f1[6] = Floor1CIU7(
		dateTime=timezone.now(), switch=data["us"][6]["switch"],temperature=data["us"][6]["temperature"], setTemp=data["us"][6]["set_temp"],
		opMode=data["us"][6]["op_mode"],airFlow=data["us"][6]["air_flow"],state=data["us"][6]["state"],
		)
	f1[7] = Floor1CIU8(
		dateTime=timezone.now(), switch=data["us"][7]["switch"],temperature=data["us"][7]["temperature"], setTemp=data["us"][7]["set_temp"],
		opMode=data["us"][7]["op_mode"],airFlow=data["us"][7]["air_flow"],state=data["us"][7]["state"],
		)
	f1[8] = Floor1CIU9(
		dateTime=timezone.now(), switch=data["us"][8]["switch"],temperature=data["us"][8]["temperature"], setTemp=data["us"][8]["set_temp"],
		opMode=data["us"][8]["op_mode"],airFlow=data["us"][8]["air_flow"],state=data["us"][8]["state"],
		)
	f1[9] = Floor1CIU10(
		dateTime=timezone.now(), switch=data["us"][9]["switch"],temperature=data["us"][9]["temperature"], setTemp=data["us"][9]["set_temp"],
		opMode=data["us"][9]["op_mode"],airFlow=data["us"][9]["air_flow"],state=data["us"][9]["state"],
		)
	f1[10] = Floor1CIU11(
		dateTime=timezone.now(), switch=data["us"][10]["switch"],temperature=data["us"][10]["temperature"], setTemp=data["us"][10]["set_temp"],
		opMode=data["us"][10]["op_mode"],airFlow=data["us"][10]["air_flow"],state=data["us"][10]["state"],
		)
	f1[11] = Floor1CIU12(
		dateTime=timezone.now(), switch=data["us"][11]["switch"],temperature=data["us"][11]["temperature"], setTemp=data["us"][11]["set_temp"],
		opMode=data["us"][11]["op_mode"],airFlow=data["us"][11]["air_flow"],state=data["us"][11]["state"],
		)
	f1[12] = Floor1CIU13(
		dateTime=timezone.now(), switch=data["us"][12]["switch"],temperature=data["us"][12]["temperature"], setTemp=data["us"][12]["set_temp"],
		opMode=data["us"][12]["op_mode"],airFlow=data["us"][12]["air_flow"],state=data["us"][12]["state"],
		)
	f1[13] = Floor1CIU14(
		dateTime=timezone.now(), switch=data["us"][13]["switch"],temperature=data["us"][13]["temperature"], setTemp=data["us"][13]["set_temp"],
		opMode=data["us"][13]["op_mode"],airFlow=data["us"][13]["air_flow"],state=data["us"][13]["state"],
		)
	for f in f1:
		f.save()
	f1s = Floor1CIUs (
			u1=f1[0],
			u2=f1[1],
			u3=f1[2],
			u4=f1[3],
			u5=f1[4],
			u6=f1[5],
			u7=f1[6],
			u8=f1[7],
			u9=f1[8],
			u10=f1[9],
			u11=f1[10],
			u12=f1[11],
			u13=f1[12],
			u14=f1[13]
		).save()
	return True

def save_ciu2(data):
	f2 = [None]*12
	f2[0] = Floor2CIU1(
		dateTime=timezone.now(), switch=data["us"][0]["switch"],temperature=data["us"][0]["temperature"], setTemp=data["us"][0]["set_temp"],
		opMode=data["us"][0]["op_mode"],airFlow=data["us"][0]["air_flow"],state=data["us"][0]["state"],
		)
	f2[1] = Floor2CIU2(
		dateTime=timezone.now(), switch=data["us"][1]["switch"],temperature=data["us"][1]["temperature"], setTemp=data["us"][1]["set_temp"],
		opMode=data["us"][1]["op_mode"],airFlow=data["us"][1]["air_flow"],state=data["us"][1]["state"],
		)
	f2[2] = Floor2CIU3(
		dateTime=timezone.now(), switch=data["us"][2]["switch"],temperature=data["us"][2]["temperature"], setTemp=data["us"][2]["set_temp"],
		opMode=data["us"][2]["op_mode"],airFlow=data["us"][2]["air_flow"],state=data["us"][2]["state"],
		)
	f2[3] = Floor2CIU4(
		dateTime=timezone.now(), switch=data["us"][3]["switch"],temperature=data["us"][3]["temperature"], setTemp=data["us"][3]["set_temp"],
		opMode=data["us"][3]["op_mode"],airFlow=data["us"][3]["air_flow"],state=data["us"][3]["state"],
		)
	f2[4] = Floor2CIU5(
		dateTime=timezone.now(), switch=data["us"][4]["switch"],temperature=data["us"][4]["temperature"], setTemp=data["us"][4]["set_temp"],
		opMode=data["us"][4]["op_mode"],airFlow=data["us"][4]["air_flow"],state=data["us"][4]["state"],
		)
	f2[5] = Floor2CIU6(
		dateTime=timezone.now(), switch=data["us"][5]["switch"],temperature=data["us"][5]["temperature"], setTemp=data["us"][5]["set_temp"],
		opMode=data["us"][5]["op_mode"],airFlow=data["us"][5]["air_flow"],state=data["us"][5]["state"],
		)
	f2[6] = Floor2CIU7(
		dateTime=timezone.now(), switch=data["us"][6]["switch"],temperature=data["us"][6]["temperature"], setTemp=data["us"][6]["set_temp"],
		opMode=data["us"][6]["op_mode"],airFlow=data["us"][6]["air_flow"],state=data["us"][6]["state"],
		)
	f2[7] = Floor2CIU8(
		dateTime=timezone.now(), switch=data["us"][7]["switch"],temperature=data["us"][7]["temperature"], setTemp=data["us"][7]["set_temp"],
		opMode=data["us"][7]["op_mode"],airFlow=data["us"][7]["air_flow"],state=data["us"][7]["state"],
		)
	f2[8] = Floor2CIU9(
		dateTime=timezone.now(), switch=data["us"][8]["switch"],temperature=data["us"][8]["temperature"], setTemp=data["us"][8]["set_temp"],
		opMode=data["us"][8]["op_mode"],airFlow=data["us"][8]["air_flow"],state=data["us"][8]["state"],
		)
	f2[9] = Floor2CIU10(
		dateTime=timezone.now(), switch=data["us"][9]["switch"],temperature=data["us"][9]["temperature"], setTemp=data["us"][9]["set_temp"],
		opMode=data["us"][9]["op_mode"],airFlow=data["us"][9]["air_flow"],state=data["us"][9]["state"],
		)
	f2[10] = Floor2CIU11(
		dateTime=timezone.now(), switch=data["us"][10]["switch"],temperature=data["us"][10]["temperature"], setTemp=data["us"][10]["set_temp"],
		opMode=data["us"][10]["op_mode"],airFlow=data["us"][10]["air_flow"],state=data["us"][10]["state"],
		)
	f2[11] = Floor2CIU12(
		dateTime=timezone.now(), switch=data["us"][11]["switch"],temperature=data["us"][11]["temperature"], setTemp=data["us"][11]["set_temp"],
		opMode=data["us"][11]["op_mode"],airFlow=data["us"][11]["air_flow"],state=data["us"][11]["state"],
		)

	for f in f2:
		f.save()
	f2s = Floor2CIUs (
			u1=f2[0],
			u2=f2[1],
			u3=f2[2],
			u4=f2[3],
			u5=f2[4],
			u6=f2[5],
			u7=f2[6],
			u8=f2[7],
			u9=f2[8],
			u10=f2[9],
			u11=f2[10],
			u12=f2[11]
		).save()
	return True

def save_ciu3(data):
	f3 = [None]*12
	f3[0] = Floor3CIU1(
		dateTime=timezone.now(), switch=data["us"][0]["switch"],temperature=data["us"][0]["temperature"], setTemp=data["us"][0]["set_temp"],
		opMode=data["us"][0]["op_mode"],airFlow=data["us"][0]["air_flow"],state=data["us"][0]["state"],
		)
	f3[1] = Floor3CIU2(
		dateTime=timezone.now(), switch=data["us"][1]["switch"],temperature=data["us"][1]["temperature"], setTemp=data["us"][1]["set_temp"],
		opMode=data["us"][1]["op_mode"],airFlow=data["us"][1]["air_flow"],state=data["us"][1]["state"],
		)
	f3[2] = Floor3CIU3(
		dateTime=timezone.now(), switch=data["us"][2]["switch"],temperature=data["us"][2]["temperature"], setTemp=data["us"][2]["set_temp"],
		opMode=data["us"][2]["op_mode"],airFlow=data["us"][2]["air_flow"],state=data["us"][2]["state"],
		)
	f3[3] = Floor3CIU4(
		dateTime=timezone.now(), switch=data["us"][3]["switch"],temperature=data["us"][3]["temperature"], setTemp=data["us"][3]["set_temp"],
		opMode=data["us"][3]["op_mode"],airFlow=data["us"][3]["air_flow"],state=data["us"][3]["state"],
		)
	f3[4] = Floor3CIU5(
		dateTime=timezone.now(), switch=data["us"][4]["switch"],temperature=data["us"][4]["temperature"], setTemp=data["us"][4]["set_temp"],
		opMode=data["us"][4]["op_mode"],airFlow=data["us"][4]["air_flow"],state=data["us"][4]["state"],
		)
	f3[5] = Floor3CIU6(
		dateTime=timezone.now(), switch=data["us"][5]["switch"],temperature=data["us"][5]["temperature"], setTemp=data["us"][5]["set_temp"],
		opMode=data["us"][5]["op_mode"],airFlow=data["us"][5]["air_flow"],state=data["us"][5]["state"],
		)
	f3[6] = Floor3CIU7(
		dateTime=timezone.now(), switch=data["us"][6]["switch"],temperature=data["us"][6]["temperature"], setTemp=data["us"][6]["set_temp"],
		opMode=data["us"][6]["op_mode"],airFlow=data["us"][6]["air_flow"],state=data["us"][6]["state"],
		)
	f3[7] = Floor3CIU8(
		dateTime=timezone.now(), switch=data["us"][7]["switch"],temperature=data["us"][7]["temperature"], setTemp=data["us"][7]["set_temp"],
		opMode=data["us"][7]["op_mode"],airFlow=data["us"][7]["air_flow"],state=data["us"][7]["state"],
		)
	f3[8] = Floor3CIU9(
		dateTime=timezone.now(), switch=data["us"][8]["switch"],temperature=data["us"][8]["temperature"], setTemp=data["us"][8]["set_temp"],
		opMode=data["us"][8]["op_mode"],airFlow=data["us"][8]["air_flow"],state=data["us"][8]["state"],
		)
	f3[9] = Floor3CIU10(
		dateTime=timezone.now(), switch=data["us"][9]["switch"],temperature=data["us"][9]["temperature"], setTemp=data["us"][9]["set_temp"],
		opMode=data["us"][9]["op_mode"],airFlow=data["us"][9]["air_flow"],state=data["us"][9]["state"],
		)
	f3[10] = Floor3CIU11(
		dateTime=timezone.now(), switch=data["us"][10]["switch"],temperature=data["us"][10]["temperature"], setTemp=data["us"][10]["set_temp"],
		opMode=data["us"][10]["op_mode"],airFlow=data["us"][10]["air_flow"],state=data["us"][10]["state"],
		)
	f3[11] = Floor3CIU12(
		dateTime=timezone.now(), switch=data["us"][11]["switch"],temperature=data["us"][11]["temperature"], setTemp=data["us"][11]["set_temp"],
		opMode=data["us"][11]["op_mode"],airFlow=data["us"][11]["air_flow"],state=data["us"][11]["state"],
		)

	for f in f3:
		f.save()
	f3s = Floor3CIUs (
			u1=f3[0],
			u2=f3[1],
			u3=f3[2],
			u4=f3[3],
			u5=f3[4],
			u6=f3[5],
			u7=f3[6],
			u8=f3[7],
			u9=f3[8],
			u10=f3[9],
			u11=f3[10],
			u12=f3[11]
		).save()
	return True
