#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
import simplejson as json
from django.core import serializers, management
from django.utils import timezone
import os, myproject.settings
from os.path import isfile
from django.db.models import Q
from .models import *
import controller
from django.views.decorators.csrf import csrf_exempt


import logging
log = logging.getLogger(__name__)

op_mode = 'AT'
flag = 0
file_path = os.path.join(myproject.settings.BASE_DIR, 'share/')
save_time = timezone.now()
save_interval = 60	# minutes

@csrf_exempt
@login_required
def index(request):
	check_if_error_exist()
	response_data = {}
	
	# 실내기 db
	floor = request.POST.get('floor','1')
	response_data.update(controller.get_CIU_from_json(floor))
	response_data.update({'floor':floor})

	# ciu - hp
	no_hp = request.POST.get('no_hp','1')
	# response_data.update(controller.get_CIU_on_HP(no_hp))
	response_data.update(controller.get_CIU_on_HP_from_json(no_hp))

	# 센서값 읽어오기
	op_mode = request.POST.get('opMode', 'AT').encode('utf-8')
	temp_mode = request.POST.get('tempMode', 'CL').encode('utf-8')
	response_data.update(controller.read_data_from_json(op_mode))
	if response_data == False:
		response_data = {"error":"file read error"}
		url = 'error/read.html'
		return render(request, url, response_data)


	# 기기 동작 내역
	selected = int(request.POST.get('page', 1))
	response_data.update(controller.get_operation_log(selected))

	# csrf token
	response_data.update(csrf(request))
	response_data.update({"error": "main"})
	url = 'monitor/index.html'
	return render(request, url, response_data)


def check_if_error_exist():
	file = file_path + 'errorlog.json'
	if isfile(file):
		with open(file) as data_file:
			response_data = json.load(data_file)
		os.remove(file)
		url = 'error/errorright_bottom.html'
		html = render_to_string(url, response_data, RequestContext(request))
		return HttpResponse(html)

@csrf_exempt
@login_required
def reload_display(request):
	response_data = {}
	# check if error exist
	check_if_error_exist()
	

	# 실내기 정보 읽어오기
	floor = request.POST.get('floor','1')
	response_data.update(controller.get_CIU_from_json(floor))
	response_data.update({'floor':floor})

	# ciu - hp
	no_hp = request.POST.get('no_hp','1')
	response_data.update(controller.get_CIU_on_HP_from_json(no_hp))
	
	global flag 
	if flag: # command를 준 후에 파일을 잠시 읽지 않는다.
		import time
		time.sleep(3)
		flag = 0

	# 센서값 읽어오기
	op_mode = request.POST.get('opMode', 'AT').encode('utf-8')
	temp_mode = request.POST.get('tempMode','CL').encode('utf-8')
	response_data.update(controller.read_data_from_json(op_mode))
	if response_data.has_key("error"):
		response_data = {"error":"file read error"}
		url = 'error/read.html'
		html = render_to_string(url, response_data)
		return HttpResponse(html)

	# 기기 동작 내역
	selected = int(request.POST.get('page', 1))
	response_data.update(controller.get_operation_log(selected))


	# save time 주기마다 DB에 저장
	global save_time
	# log.debug("save_time: " + str(save_time))
	if (timezone.now() - save_time) > timezone.timedelta(minutes=save_interval):
		# log.debug(timezone.now() - save_time)
		if not controller.save_data(response_data):
			# DB save 에러
			pass
		response_data.update(controller.get_CIU_from_json(1))
		controller.save_ciu1(response_data)
		response_data.update(controller.get_CIU_from_json(2))
		controller.save_ciu2(response_data)
		response_data.update(controller.get_CIU_from_json(3))
		controller.save_ciu3(response_data)
		log.debug("database updated")
		save_time = timezone.now()

	# log.debug(response_data)
	url = 'monitor/container.html'
	html = render_to_string(url, response_data, RequestContext(request))
	return HttpResponse(html)

@login_required
def specs(request):
	response_data = controller.get_device_specs()
	url = 'monitor/specs.html'
	return render(request, url, response_data)

@login_required
def setting_cp(request):
	response_data = {}
	url = 'monitor/setting_cp.html'
	return render(request, url, response_data)

@login_required
def show_database(request):
	response_data = {}
	url = 'monitor/show_database.html'
	return render(request, url, response_data)

@login_required
def set_cp(request):
	response_data = {}
	cpid = int(request.POST.get('cpid', 1))
	op_mode = request.POST.get('opMode', 'AT').encode('utf-8')
	cpswitch = request.POST.get('cpswitch', 'error').encode('utf-8')
	cphz = int(request.POST.get('cphz', 0))
	cpflux = int(request.POST.get('cpflux', 0))
	temp_mode = request.POST.get('tempMode', 'CL').encode('utf-8')
	# 설정 값 db에 저장
	controller.set_cp(cpid, op_mode, cpswitch, cphz, cpflux)
	# cmdmain에 기록
	controller.write_cmd(temp_mode, op_mode)
	

	# check if error exist
	check_if_error_exist()

	global flag 
	if flag: # command를 준 후에 파일을 잠시 읽지 않는다.
		import time
		time.sleep(2)
		flag = 0

	# 센서값 읽어오기
	op_mode = request.POST.get('op_mode', 'error').encode('utf-8')
	temp_mode = request.POST.get('tempMode', 'CL').encode('utf-8')
	response_data = controller.read_data_from_json(op_mode)
	if response_data == False:
		response_data = {"error":"file read error"}
		url = 'error/read.html'
		html = render_to_string(url, response_data)
		return HttpResponse(html)

	# 기기 동작 내역
	selected = int(request.POST.get('page', 1))
	response_data.update(controller.get_operation_log(selected))

	html = render_to_string('monitor/container.html', response_data, RequestContext(request))
	return HttpResponse(html)

@login_required
def page_request(request):
	if not request.POST:
		return render_to_response('monitor/container.html',context_instance=RequestContext(request))

	# 기기 동작 내역
	selected = int(request.POST.get('page', 1))
	response_data = controller.get_operation_log(selected)

	html = render_to_string('monitor/right_bottom.html', response_data, RequestContext(request))
    	return HttpResponse(html)

@login_required
def toggle_switch(request):
	if not request.POST:
		return render_to_response('monitor/container.html', context_instance=RequestContext(request))

	location = request.POST.get('id', 'error').split('-')[0]
	loc = location.upper()
	switch_status = request.POST.get('status', 'error').encode('utf-8').upper()

	op_mode = request.POST.get('opMode', 'AT').encode('utf-8')
	temp_mode = request.POST.get('tempMode', 'CL').encode('utf-8')

	# 심정 펌프 갱신
	dwp = ''
	if loc == 'DWP1': 
		dwp = DeepwellPump1Logger(
			dateTime=timezone.now(), opMode=op_mode, switch=switch_status
		)
	elif loc == 'DWP2':
		dwp = DeepwellPump2Logger(
			dateTime=timezone.now(), opMode=op_mode, switch=switch_status
		)
	elif loc == 'DWP3':
		dwp = DeepwellPump3Logger(
			dateTime=timezone.now(), opMode=op_mode, switch=switch_status
		)
	elif loc == 'DWP4':
		dwp = DeepwellPump4Logger(
			dateTime=timezone.now(), opMode=op_mode, switch=switch_status
		)
	if dwp != '':
		dwp.save()


	# 기기 동작 내역 갱신
	new_cmd = OperationSwitchControl(
			dateTime=timezone.now(), location=loc, switch=switch_status
		)
	new_cmd.save()

	# 커맨드 파일 작성
	controller.write_cmd(temp_mode, op_mode)
	# 커맨드 후 hmidata를 잠시동안 읽지 않는다.
	global flag 
	flag = int(request.POST.get('flag', '0'))

	# 기기 동작 내역
	response_data = controller.get_operation_log(1)
	
	html = render_to_string('monitor/right_bottom.html', response_data, RequestContext(request))
	return HttpResponse(html)


def floor_change(request):
	if not request.POST:
		return render_to_response('monitor/container.html', context_instance=RequestContext(request))

	response_data = {}
	# 실내기 정보 읽어오기
	floor = request.POST.get('floor', '1')
	response_data.update(controller.get_CIU_from_json(floor))
	response_data.update({'floor':floor})
	
	html = render_to_string('monitor/floor.html', response_data, RequestContext(request))
	return HttpResponse(html)


def change_ciuonhp(request):
	if not request.POST:
		return render_to_response('monitor/container.html', context_instance=RequestContext(request))

	response_data = {}
	# ciu - hp 정보
	no_hp = request.POST.get('no_hp','1')
	response_data.update(controller.get_CIU_on_HP(no_hp))

	html = render_to_string('monitor/right_bottom.html', response_data, RequestContext(request))
	return HttpResponse(html)

# @login_required
# def show_database(request):
# 	if not request.POST:
# 		return render_to_response('monitor/container.html', context_instance=RequestContext(request))

# 	response_data = {}
# 	id = request.POST.get('id', 'None')
# 	start_date = timezone.now() - datetime.timedelta(days=7)
# 	end_date = timezone.now()

# 	# 온도 센서
# 	if id == 'TempHEIn1':
# 		database = TempHEIn1Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'TempHEIn2':
# 		database = TempHEIn2Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'TempHEOut1'\
# 	or id == 'TempHPIn1' or id == 'TempHPIn2' or id == 'TempHPIn3'\
# 	or id == 'TempHPIn4' or id == 'TempHPIn5' or id == 'TempHPIn6':
# 		database = TempHEOut1Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'TempHEOut2':
# 		database = TempHEOut2Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'TempHPOut1':
# 		database = TempHPOut1Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'TempHPOut2':
# 		database = TempHPOut2Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'TempHPOut3':
# 		database = TempHPOut3Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'TempHPOut4':
# 		database = TempHPOut4Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'TempHPOut5':
# 		database = TempHPOut5Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'TempHPOut6':
# 		database = TempHPOut6Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	# 순환 펌프
# 	elif id == 'CirculatingPump':
# 		database = CirculatingPumpLogger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	# 순환 유량계
# 	elif id == 'CPFlowmeter':
# 		database = CPFlowmeterLogger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	# 심정 유량계
# 	elif id == 'DWPFlowmeter':
# 		database = DWPFlowmeterLogger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	# 심정 펌프
# 	elif id == 'DeepwellPump1':
# 		database = DeepwellPump1Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'DeepwellPump2':
# 		database = DeepwellPump2Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'DeepwellPump3':
# 		database = DeepwellPump3Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	elif id == 'DeepwellPump4':
# 		database = DeepwellPump4Logger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	# rt
# 	elif id == 'RefrigerationTon':
# 		database = RefrigerationTonLogger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	# 전력량
# 	elif id == 'PowerConsumption':
# 		database = PowerConsumptionLogger.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
# 	else:
# 		database = 'None'
# 	response_data.update({'id': id})
# 	response_data.update({'database': database})
# 	# csrf token
# 	response_data.update(csrf(request))
# 	html = render_to_string('monitor/sensor_data.html', response_data, RequestContext(request))
# 	# log.debug(html)
# 	return HttpResponse(html)


@login_required
def setting_mode(request):
	html = render_to_response('monitor/setting_mode.html',{}, RequestContext(request))
	return HttpResponse(html)

@login_required
def setting_mode_confirm(request):
	op_mode = request.POST.get('opMode', 'error')
	if op_mode == 'error':
		return HttpResponseRedirect('/')

	response_data = {}
	# check if error exist
	check_if_error_exist()

	if op_mode == 'AT':
		# 전체화면
		return reload_display(request)
	else :# op_mode == 'MN'
		return operation_control(request)

@login_required	
def operation_control(request):
	response_data = {}
	response_data.update(controller.read_data_from_json(op_mode))

	if response_data.has_key("error"):
		log.debug("error")
		response_data = {"error":"file read error"}
		url = 'error/read.html'
		html = render_to_string(url, response_data)
		return HttpResponse(html)

	html = render_to_string('monitor/operation_control.html', response_data, RequestContext(request))
	return HttpResponse(html)


# DB 검색
def search_db_ciu(request):
	html = render_to_string('monitor/search_db_ciu.html', {}, RequestContext(request))
	return HttpResponse(html)

def search_db_ciu_result(request):
	start_date = request.POST.get('startDate', 'error')
	end_date = request.POST.get('endDate', 'error')
	floor = request.POST.get('floor', '0')
	name = request.POST.get('name', '0')
	is_1st_all = is_2nd_all = is_3rd_all = False

	if floor == '1':
		if name == '1':
			database = Floor1CIU1.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		elif name == '2':
			database = Floor1CIU2.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		elif name == '3':
			database = Floor1CIU3.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '4':
			database = Floor1CIU4.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '5':
			database = Floor1CIU5.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '6':
			database = Floor1CIU6.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '7':
			database = Floor1CIU7.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '8':
			database = Floor1CIU8.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '9':
			database = Floor1CIU9.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '10':
			database = Floor1CIU10.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '11':
			database = Floor1CIU11.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '12':
			database = Floor1CIU12.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '13':
			database = Floor1CIU13.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '14':
			database = Floor1CIU14.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		else: # (전체)
			d1 = Floor1CIU1.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
			d2 = Floor1CIU2.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
			d3 = Floor1CIU3.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d4 = Floor1CIU4.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d5 = Floor1CIU5.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d6 = Floor1CIU6.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d7 = Floor1CIU7.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d8 = Floor1CIU8.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d9 = Floor1CIU9.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d10 = Floor1CIU10.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d11 = Floor1CIU11.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d12 = Floor1CIU12.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d13 = Floor1CIU13.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d14 = Floor1CIU14.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			database1 = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]
			response_data = {"database":database1}

	elif floor == '2':
		if name == '1':
			database = Floor2CIU1.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		elif name == '2':
			database = Floor2CIU2.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		elif name == '3':
			database = Floor2CIU3.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '4':
			database = Floor2CIU4.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '5':
			database = Floor2CIU5.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '6':
			database = Floor2CIU6.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '7':
			database = Floor2CIU7.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '8':
			database = Floor2CIU8.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '9':
			database = Floor2CIU9.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '10':
			database = Floor2CIU10.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '11':
			database = Floor2CIU11.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '12':
			database = Floor2CIU12.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		else: # (전체)
			d1 = Floor2CIU1.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
			d2 = Floor2CIU2.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
			d3 = Floor2CIU3.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d4 = Floor2CIU4.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d5 = Floor2CIU5.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d6 = Floor2CIU6.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d7 = Floor2CIU7.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d8 = Floor2CIU8.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d9 = Floor2CIU9.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d10 = Floor2CIU10.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d11 = Floor2CIU11.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d12 = Floor2CIU12.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			database2 = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
			response_data = {"database":database2}
	elif floor == '3':
		if name == '1':
			database = Floor3CIU1.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		elif name == '2':
			database = Floor3CIU2.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		elif name == '3':
			database = Floor3CIU3.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '4':
			database = Floor3CIU4.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '5':
			database = Floor3CIU5.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '6':
			database = Floor3CIU6.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '7':
			database = Floor3CIU7.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '8':
			database = Floor3CIU8.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '9':
			database = Floor3CIU9.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '10':
			database = Floor3CIU10.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '11':
			database = Floor3CIU11.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		elif name == '12':
			database = Floor3CIU12.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		else: # (전체)
			d1 = Floor3CIU1.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
			d2 = Floor3CIU2.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
			d3 = Floor3CIU3.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d4 = Floor3CIU4.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d5 = Floor3CIU5.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d6 = Floor3CIU6.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d7 = Floor3CIU7.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d8 = Floor3CIU8.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d9 = Floor3CIU9.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d10 = Floor3CIU10.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d11 = Floor3CIU11.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			d12 = Floor3CIU12.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
			database3 = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
			response_data = {"database":database3}
	else: # (전체)
		d1 = Floor1CIU1.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		d2 = Floor1CIU2.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		d3 = Floor1CIU3.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d4 = Floor1CIU4.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d5 = Floor1CIU5.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d6 = Floor1CIU6.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d7 = Floor1CIU7.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d8 = Floor1CIU8.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d9 = Floor1CIU9.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d10 = Floor1CIU10.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d11 = Floor1CIU11.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d12 = Floor1CIU12.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d13 = Floor1CIU13.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d14 = Floor1CIU14.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		database1 = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]
		d1 = Floor2CIU1.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		d2 = Floor2CIU2.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		d3 = Floor2CIU3.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d4 = Floor2CIU4.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d5 = Floor2CIU5.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d6 = Floor2CIU6.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d7 = Floor2CIU7.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d8 = Floor2CIU8.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d9 = Floor2CIU9.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d10 = Floor2CIU10.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d11 = Floor2CIU11.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d12 = Floor2CIU12.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		database2 = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
		d1 = Floor3CIU1.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		d2 = Floor3CIU2.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date)) 
		d3 = Floor3CIU3.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d4 = Floor3CIU4.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d5 = Floor3CIU5.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d6 = Floor3CIU6.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d7 = Floor3CIU7.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d8 = Floor3CIU8.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d9 = Floor3CIU9.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d10 = Floor3CIU10.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d11 = Floor3CIU11.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		d12 = Floor3CIU12.objects.filter(Q(dateTime__gte=start_date), Q(dateTime__lte=end_date))
		database3 = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
		database_list = [database1,database2,database3]
		response_data = {"database_list":database_list}

	if 'response_data' not in locals():
		response_data = {"database":[database]}

	url = 'monitor/search_db_ciu_result.html'
	html = render_to_string(url, response_data, RequestContext(request))
	return HttpResponse(html)



