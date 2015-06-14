from django.shortcuts import render

from .models import OperationLogger, TemperatureLogger, Flo 연결wmeterLogger

def index(request):
	latest_operation_data = OperationLogger.objects.latest('date')
	latest_temperature_data = TemperatureLogger.objects.latest('date')
	latest_flowmeter_data = FlowmeterLogger.objects.latest('date')

	switched = check_operation()
	url = 'index.html'
	context = {
		"operation_data": latest_operation_data,
		"temperature_data": latest_temperature_data,
		"flowmeter_data": latest_flowmeter_data,
	}
	return render(request, url, context)
