#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.template.context_processors import csrf
import simplejson as json
from django.utils import timezone
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage
# from django.forms.models import model_to_dict

from .models import *
# import watchdir
import os, myproject.settings


logs_per_page = 10
page_no = 5

file = 'share/commands.txt'
filepath = os.path.join(myproject.settings.BASE_DIR, file)


def index(request):
	global logs_per_page
	global page_no

	# watchdir.file_watch('share/')

	latest_operation = OperationLogger.objects.latest('dateTime')
	latest_temperature = TemperatureLogger.objects.latest('dateTime')
	latest_flowmeter = DWPFlowmeterLogger.objects.latest('dateTime')

	switch_list = OperationSwitchControl.objects.order_by('-dateTime')
	paginator = Paginator(switch_list, logs_per_page)
	selected=1
	switch_logs = paginator.page(selected)
	page_range = range(selected,selected+9)


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
	inverter = InverterLogger.objects.latest('dateTime')

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

	url = 'index.html'
	response_data = {
		"operation": latest_operation,
		"temperature": latest_temperature,
		"flowmeter": latest_flowmeter,
		"switch_logs": switch_logs,
		"page_range": page_range,
		"selected": selected,

		"heat_pump": heat_pump,
		"DWP": DWP,
		"circulating_pump": circulating_pump,
		"inverter": inverter,
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
	}
	return render(request, url, response_data)


def specs(request):
	url = 'specs.html'
	response_data = {

	}
	return render(request, url, response_data)


def hmi_insert_data(request):
	return;

def ajax_page_request(request):
	if not request.POST:
		return render_to_response('index.html',context_instance=RequestContext(request))

	global logs_per_page, page_no

	# pagination
	selected = int(request.POST.get('selected', 0))
	switch_list = OperationSwitchControl.objects.order_by('-dateTime')
	paginator = Paginator(switch_list, logs_per_page)

	# 선택된 페이지가 범위를 초과된 경우 (prev, next 선택)
	if (selected < 0):
		selected=1
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

	response_data = {
		"switch_logs": switch_logs,
		"page_range": page_range,
		"selected": selected,
	}
	response_data.update(csrf(request))
	html = render_to_string('log.html', response_data)
    	return HttpResponse(html)


def ajax_index_reload(request):
	if not request.POST:
		return render_to_response('index.html', context_instance=RequestContext(request))

	latest_operation_data = OperationLogger.objects.latest('dateTime')
	latest_temperature_data = TemperatureLogger.objects.latest('dateTime')
	latest_flowmeter_data = DWPFlowmeterLogger.objects.latest('dateTime')

	response_data = {
		"operation_data": latest_operation_data,
		"temperature_data": latest_temperature_data,
		"flowmeter_data": latest_flowmeter_data,
	}
	response_data.update(csrf(request))
	html = render_to_string('left.html', response_data)
    	return HttpResponse(html)


def ajax_set_operation_mode(request):
	if not request.POST:
		return render_to_response('index.html', context_instance=RequestContext(request))

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
		return render_to_response('index.html', context_instance=RequestContext(request))

	location = request.POST.get('id', 'error').split('-')[0]
	loc = location.upper()
	switch_status = request.POST.get('status', 'error').encode('utf-8').upper()

	new_cmd = OperationSwitchControl(
			dateTime=timezone.now(), location=loc, switch=switch_status
		)
	new_cmd.save()

	global logs_per_page
	# queryset to dict list
	# queryset = OperationSwitchControl.objects.order_by('-dateTime')[:logs_per_page]
	# single_data_list = [None]*logs_per_page
	# for i, obj in zip(range(logs_per_page), queryset):
	# 	single_data_list[i] = queryset[i].__dict__


	switch_list = OperationSwitchControl.objects.order_by('-dateTime')
	paginator = Paginator(switch_list, logs_per_page)
	selected=1
	switch_logs = paginator.page(selected)
	page_range = range(selected,selected+9)


	####### create json file
	temp_mode = request.POST.get('tempMode', 'temp error').encode('utf-8')
	op_mode = request.POST.get('opMode', 'op error').encode('utf-8')
	cp = InverterLogger.objects.latest('id')
	dwp1 = DeepwellPump1Logger.objects.latest('id')
	dwp2 = DeepwellPump1Logger.objects.latest('id')
	dwp3 = DeepwellPump1Logger.objects.latest('id')
	dwp4 = DeepwellPump1Logger.objects.latest('id')
	rt = RefrigerationTonLogger.objects.latest('id')
	datetime = str(timezone.now())[:-7]
	cmd_text = {
		'temp_mode': temp_mode,
		'op_mode': op_mode,
		'cp': cp.switch,
		'cp_id': cp.inverterID,
		'cp_rpm': cp.RPM,
		'inverter_hz': cp.Hz,
		'dwp1': dwp1.switch,
		'dwp2': dwp2.switch,
		'dwp3': dwp3.switch,
		'dwp4': dwp4.switch,
		'rt': rt.RT,
		'datetime':datetime,
	}
	fp = open('share/cmdmain.json', 'w')
	json.dump(cmd_text, fp)



	response_data = {
		"switch_logs": switch_logs,
		"page_range": page_range,
		"selected": selected,
	}
	response_data.update(csrf(request))
	html = render_to_string('log.html', response_data)
    	return HttpResponse(html)
