#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.template.context_processors import csrf
import simplejson as json
from django.core import serializers, management
from django.utils import timezone
import os, myproject.settings
from os.path import isfile
from .models import *
import db_controller

import logging
log = logging.getLogger(__name__)

flag = 0
file_path = os.path.join(myproject.settings.BASE_DIR, 'share\\')
save_time = timezone.now()
save_interval = 60	# minutes

def index(request):
	response_data = {}

	check_if_error_exist()
	
	# 실내기 db
	floor = request.POST.get('floor',1)
	response_data.update(db_controller.get_CIU(floor))

	# 센서값 읽어오기
	op_mode = request.POST.get('opMode', 'AT').encode('utf-8')
	temp_mode = request.POST.get('tempMode', 'CL').encode('utf-8')
	response_data.update(db_controller.read_data_from_json(op_mode, temp_mode))
	if response_data == False:
		response_data = {"error":"file read error"}
		url = 'error/read.html'
		return render(request, url, response_data)


	# 기기 동작 내역
	selected = int(request.POST.get('page', 1))
	response_data.update(db_controller.get_operation_log(selected))
	# response_data = response_data.iteritems()
	url = 'monitor/index.html'
	return render(request, url, response_data)

def ajax_reload_display(request):
	if not request.POST:
		return HttpResponseRedirect('/')

	response_data = {}
	# check if error exist
	check_if_error_exist()
	

	# 실내기 정보 읽어오기
	floor = request.POST.get('floor',1)
	response_data.update(db_controller.get_CIU_from_json(floor))

	
	global flag 
	if flag: # command를 준 후에 파일을 잠시 읽지 않는다.
		import time
		time.sleep(3)
		flag = 0

	# 센서값 읽어오기
	op_mode = request.POST.get('opMode', 'AT').encode('utf-8')
	temp_mode = request.POST.get('tempMode','CL').encode('utf-8')
	response_data.update(db_controller.read_data_from_json(op_mode, temp_mode))
	if response_data.has_key("error"):
		response_data = {"error":"file read error"}
		url = 'error/read.html'
		html = render_to_string(url, response_data)
		return HttpResponse(html)

	# 기기 동작 내역
	selected = int(request.POST.get('page', 1))
	response_data.update(db_controller.get_operation_log(selected))


	# save time 주기마다 DB에 저장
	if (timezone.now() - save_time) > timezone.timedelta(minutes=save_interval):
		if not db_controller.save_data(response_data):
			# DB save 에러
			pass


	# csrf token
	response_data.update(csrf(request))
	# log.debug(response_data)
	html = render_to_string('monitor/container.html', response_data)
	return HttpResponse(html)

def ajax_reload_data(request):
	if not request.POST:
		return render_to_response('monitor/container.html', context_instance=RequestContext(request))

	if(db_controller.save_data()):
		response_data = db_controller.get_sensors()
		response_data.update(csrf(request))
		html = render_to_string('monitor/container.html', response_data)
		return HttpResponse(html)
	else:
		from django.contrib.auth import logout
		logout(request)
		return HttpResponseRedirect('/')


def specs(request):
	response_data = db_controller.get_device_specs()
	url = 'monitor/specs.html'
	return render(request, url, response_data)


def cp_setting(request):
	response_data = {}
	url = 'monitor/cp_setting.html'
	return render(request, url, response_data)

def ajax_set_cp(request):
	response_data = {}
	cpid = int(request.POST.get('cpid', 1))
	op_mode = request.POST.get('opMode', 'AT').encode('utf-8')
	cpswitch = request.POST.get('cpswitch', 'error').encode('utf-8')
	cphz = int(request.POST.get('cphz', 0))
	cpflux = int(request.POST.get('cpflux', 0))
	temp_mode = request.POST.get('tempMode', 'CL').encode('utf-8')
	# 설정 값 db에 저장
	db_controller.set_cp(cpid, op_mode, cpswitch, cphz, cpflux)
	# cmdmain에 기록
	db_controller.write_cmd(temp_mode, op_mode)
	

	# check if error exist
	check_if_error_exist()

	global flag 
	if flag: # command를 준 후에 파일을 잠시 읽지 않는다.
		import time
		time.sleep(3)
		flag = 0

	# 센서값 읽어오기
	op_mode = request.POST.get('op_mode', 'error').encode('utf-8')
	temp_mode = request.POST.get('tempMode', 'CL').encode('utf-8')
	response_data = db_controller.read_data_from_json(op_mode, temp_mode)
	if response_data == False:
		response_data = {"error":"file read error"}
		url = 'error/read.html'
		html = render_to_string(url, response_data)
		return HttpResponse(html)

	# 기기 동작 내역
	selected = int(request.POST.get('page', 1))
	response_data.update(db_controller.get_operation_log(selected))
	response_data.update(csrf(request))
	html = render_to_string('monitor/container.html', response_data)
	return HttpResponse(html)


def hmi_insert_data(request):
	return;


def ajax_page_request(request):
	if not request.POST:
		return render_to_response('monitor/container.html',context_instance=RequestContext(request))

	# 기기 동작 내역
	selected = int(request.POST.get('page', 1))
	response_data = db_controller.get_operation_log(selected)

	response_data.update(csrf(request))
	html = render_to_string('monitor/log.html', response_data)
    	return HttpResponse(html)


def ajax_index_reload(request):
	# if not request.POST:
	# 	return render_to_response('container.html', context_instance=RequestContext(request))

	# latest_operation_data = OperationLogger.objects.latest('dateTime')
	# latest_temperature_data = TemperatureLogger.objects.latest('dateTime')
	# latest_flowmeter_data = DWPFlowmeterLogger.objects.latest('dateTime')

	# response_data = {
	# 	"operation_data": latest_operation_data,
	# 	"temperature_data": latest_temperature_data,
	# 	"flowmeter_data": latest_flowmeter_data,
	# }
	# response_data.update(csrf(request))
	# html = render_to_string('monitor/left.html', response_data)
    	return HttpResponse(html)


def ajax_set_operation_mode(request):
	if not request.POST:
		return render_to_response('monitor/container.html', context_instance=RequestContext(request))

	opMode = request.POST.get('opMode', 'error').encode('utf-8')

	#### file write
	# try:
	# 	file_commands = open(file_path,'w')
	# except IOError as e:
	# 	print e.strerror

	# file_commands.write("opMode: "+opMode)
	# file_commands.close()
	####

	response_data = {
		"opMode": opMode,
	}
	return HttpResponse(json.dumps(response_data), content_type="application/json")



def ajax_toggle_switch(request):
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
	db_controller.write_cmd(temp_mode, op_mode)
	# 커맨드 후 hmidata를 잠시동안 읽지 않는다.
	global flag 
	flag = int(request.POST.get('flag', '0'))

	# 기기 동작 내역
	response_data = db_controller.get_operation_log(1)
	response_data.update(csrf(request))
	html = render_to_string('monitor/log.html', response_data)
	return HttpResponse(html)


def ajax_floor_change(request):
	if not request.POST:
		return render_to_response('monitor/container.html', context_instance=RequestContext(request))

	response_data = {}
	# 실내기 정보 읽어오기
	floor = int(request.POST.get('floor', "1"))
	response_data.update(db_controller.get_CIU_from_json(floor))
	# csrf token
	response_data.update(csrf(request))
	html = render_to_string('monitor/floor.html', response_data)
	return HttpResponse(html)


def check_if_error_exist():
	file = file_path + 'errorlog.json'
	if isfile(file):
		with open(file) as data_file:
			response_data = json.load(data_file)
		os.remove(file)
		url = 'error/errorlog.html'
		html = render_to_string(url, response_data)
		return HttpResponse(html)
