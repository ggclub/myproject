from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.template.context_processors import csrf
import json


from .models import *
import os, myproject.settings

logs_per_page = 10
page_no = 10

file = 'share/commands.txt'
filepath = os.path.join(myproject.settings.BASE_DIR, file)


def index(request):
	global logs_per_page
	global page_no

	# watchdir.file_watch('share/')

	latest_operation_data = OperationLogger.objects.latest('dateTime')
	latest_temperature_data = TemperatureLogger.objects.latest('dateTime')
	latest_flowmeter_data = DWPFlowmeterLogger.objects.latest('dateTime')
	latest_single_switch_data_list = OperationSwitchControl.objects.order_by('-dateTime')[:logs_per_page]

	total_page_no, page_no = count_page()


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
		"operation_data": latest_operation_data,
		"temperature_data": latest_temperature_data,
		"flowmeter_data": latest_flowmeter_data,
		"single_data_list": latest_single_switch_data_list,
		"total_page_no": total_page_no,
		"page_no": range(1, page_no + 1),

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


def count_page():
	page_no = 10
	total_log_no = OperationSwitchControl.objects.count()
	total_page_no = ((total_log_no-1) // logs_per_page) + 1

	if(total_page_no < page_no):
		page_no = total_page_no

	return total_page_no, page_no


def ajax_page_request(request):
	if not request.POST:
		return render_to_response('index.html',context_instance=RequestContext(request))

	global logs_per_page

	current_page = int(request.POST.get('page_index', 0))

	# latest_single_switch_data_list = OperationSwitchControl.objects.order_by('-dateTime')[:logs_per_page]
	latest_single_switch_data_list = OperationSwitchControl.objects.order_by('-dateTime')[(current_page-1)*logs_per_page:(current_page)*logs_per_page]

	total_page_no, page_no = count_page()

	response_data = {
		"single_data_list": latest_single_switch_data_list,
		"current_page": current_page,
		# "total_page_no": total_page_no,
		"page_no": range(1, page_no + 1),
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

	opMode = request.POST.get('opMode', 'error')


	#### file write
	try:
		file_commands = open(filepath,'w')
	except IOError as e:
		print e.strerror

	file_commands.write("opMode: "+opMode)
	file_commands.close()
	####

	response_data = {
		"opMode": opMode,
		# "error_message": e.strerror,
	}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

