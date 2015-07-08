from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf

import logging

# Create your views here.
def index(request):
	username = password = state = ''
	if request.method == 'POST':
		# login submit button
		if 'submit' in request.POST:
			username = request.POST.get('username')
			password = request.POST.get('password')

			
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)

				if not request.POST.get('remember', None):
					request.session.set_expiry(0)


				state = "Login success."
				url='login/success.html'
				return render(request, url, {"state":state})
			else :
				state = "incorrect username and/or password."

		# logout button
		if 'logout' in request.POST:
			logout(request)
			return HttpResponseRedirect('/')


	# if already logged in
	if request.user.is_authenticated():
		c = {}
		c.update(csrf(request))
		return render(request, 'monitor/pre.html', c)


	url='login/index.html'
	response_data = {
		'state': state,
	}
	response_data.update(csrf(request))
	return render(request, url, response_data)

