from django.shortcuts import render

from .models import OperationLogger, TemperatureLogger, FlowmeterLogger, SingleSwitchLogger

logs_per_page = 10
page_no = 10

def index(request):
	global logs_per_page
	global page_no
	# logs_per_page += 10
	# page_no += 10

	latest_operation_data = OperationLogger.objects.latest('date')
	latest_temperature_data = TemperatureLogger.objects.latest('date')
	latest_flowmeter_data = FlowmeterLogger.objects.latest('date')
	latest_single_switch_data_list = SingleSwitchLogger.objects.order_by('-date')[:logs_per_page]

	total_page_no, page_no = count_page()


	url = 'index.html'
	# url = 'hello-ng.html'
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
	# if not request.POST:
	# 	return render_to_response('index.html')

	if request.is_ajax() and request.method == 'POST':
		current_page=request.POST.get('page_index', 0)

	latest_single_switch_data_list = SingleSwitchLogger.objects.order_by('-date')[(current_page-1):(current_page-1)+logs_per_page]

	total_page_no, page_no = count_page()

	url = 'index.html'
	response_data = {
		"single_data_list": latest_single_switch_data_list,
		"current_page": current_page,
		"total_page_no": total_page_no,
		"page_no": range(1, page_no + 1),
	}
	return render(request, url, response_data)
	# auto/ajax_color_request.html
