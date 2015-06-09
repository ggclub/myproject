from django.shortcuts import render


def index(request):
	url = 'monitor/index.html'
	context = {}
	return render(request, url, context)
