#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.template.context_processors import csrf
import simplejson as json
from django.core import serializers, management
from django.utils import timezone
import os, myproject.settings
from .models import *
import db_controller




file = 'share/commands.txt'
filepath = os.path.join(myproject.settings.BASE_DIR, file)


def index(request):
	# 센서값 읽어오기
	response_data = db_controller.read_data_from_json()
	if response_data == False:
		return HttpResponseRedirect('/')

	# 기기 동작 내역
	response_data.update(db_controller.get_operation_log(1))
	url = 'monitor/index.html'
	return render(request, url, response_data)


def specs(request):
	response_data = db_controller.get_device_specs()
	url = 'monitor/specs.html'
	return render(request, url, response_data)


def hmi_insert_data(request):
	return;


def ajax_page_request(request):
	if not request.POST:
		return render_to_response('monitor/index.html',context_instance=RequestContext(request))

	# 기기 동작 내역
	selected = int(request.POST.get('selected', 0))
	response_data = db_controller.get_operation_log(selected)

	response_data.update(csrf(request))
	html = render_to_string('monitor/log.html', response_data)
    	return HttpResponse(html)


def ajax_index_reload(request):
	# if not request.POST:
	# 	return render_to_response('index.html', context_instance=RequestContext(request))

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

def ajax_reload_display(request):
	if not request.POST:
		return render_to_response('index.html', context_instance=RequestContext(request))

	# 센서 값 읽어오기
	response_data = db_controller.read_data_from_json()
	response_data.update(csrf(request))
	html = render_to_string('monitor/left.html', response_data)
	return HttpResponse(html)

def ajax_reload_data(request):
	if not request.POST:
		return render_to_response('index.html', context_instance=RequestContext(request))

	if(db_controller.save_data()):
		response_data = db_controller.get_sensors()
		response_data.update(csrf(request))
		html = render_to_string('monitor/left.html', response_data)
		return HttpResponse(html)
	else:
		return HttpResponseRedirect('/')


def ajax_set_operation_mode(request):
	if not request.POST:
		return render_to_response('monitor/index.html', context_instance=RequestContext(request))

	opMode = request.POST.get('opMode', 'error').encode('utf-8')

	#### file write
	# try:
	# 	file_commands = open(filepath,'w')
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
		return render_to_response('monitor/index.html', context_instance=RequestContext(request))

	location = request.POST.get('id', 'error').split('-')[0]
	loc = location.upper()
	switch_status = request.POST.get('status', 'error').encode('utf-8').upper()

	new_cmd = OperationSwitchControl(
			dateTime=timezone.now(), location=loc, switch=switch_status
		)
	new_cmd.save()

	# 커맨드 파일 작성
	temp_mode = request.POST.get('tempMode', 'temp error').encode('utf-8')
	op_mode = request.POST.get('opMode', 'op error').encode('utf-8')
	db_controller.write_cmd(temp_mode, op_mode)

	# 기기 동작 내역
	response_data = db_controller.get_operation_log(1)
	response_data.update(csrf(request))
	html = render_to_string('monitor/log.html', response_data)
	return HttpResponse(html)
