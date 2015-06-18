from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.template.context_processors import csrf
import json


from .models import OperationLogger, TemperatureLogger, FlowmeterLogger, SingleSwitchLogger
import watchdir
import os, myproject.settings

logs_per_page = 10
page_no = 10

file = 'share/commands.txt'
filepath = os.path.join(myproject.settings.BASE_DIR, file)


def index(request):
	global logs_per_page
	global page_no

	# watchdir.file_watch('share/')

	latest_operation_data = OperationLogger.objects.latest('date')
	latest_temperature_data = TemperatureLogger.objects.latest('date')
	latest_flowmeter_data = FlowmeterLogger.objects.latest('date')
	latest_single_switch_data_list = SingleSwitchLogger.objects.order_by('-date')[:logs_per_page]

	total_page_no, page_no = count_page()


	url = 'index.html'
	response_data = {
		"operation_data": latest_operation_data,
		"temperature_data": latest_temperature_data,
		"flowmeter_data": latest_flowmeter_data,
		"single_data_list": latest_single_switch_data_list,
		"total_page_no": total_page_no,
		"page_no": range(1, page_no + 1),
	}
	return render(request, url, response_data)


def count_page():
	page_no = 10
	total_log_no = SingleSwitchLogger.objects.count()
	total_page_no = ((total_log_no-1) // logs_per_page) + 1

	if(total_page_no < page_no):
		page_no = total_page_no

	return total_page_no, page_no


def ajax_page_request(request):
	if not request.POST:
		return render_to_response('index.html',context_instance=RequestContext(request))

	global logs_per_page

	current_page = int(request.POST.get('page_index', 0))

	# latest_single_switch_data_list = SingleSwitchLogger.objects.order_by('-date')[:logs_per_page]
	latest_single_switch_data_list = SingleSwitchLogger.objects.order_by('-date')[(current_page-1)*logs_per_page:(current_page)*logs_per_page]

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

	latest_operation_data = OperationLogger.objects.latest('date')
	latest_temperature_data = TemperatureLogger.objects.latest('date')
	latest_flowmeter_data = FlowmeterLogger.objects.latest('date')

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

	mode = request.POST.get('mode', 'error')


	#### file write
	try:
		file_commands = open(filepath,'w')
	except IOError as e:
		print e.strerror

	file_commands.write("Mode: "+mode)
	file_commands.close()
	####

	response_data = {
		"mode": mode,
		# "error_message": e.strerror,
	}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

