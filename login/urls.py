#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^logout/$', views.log_out, name='logout'),
	url(r'^change_password_page/$', views.change_password_page, name='change_password_page'),
	url(r'^change_password_done/$', views.change_password_done, name='change_password_done'),
	url(r'^on_mode_change/$', views.on_mode_change, name='on_mode_change'),
	url(r'^on_mode_confirm/$', views.on_mode_confirm, name='on_mode_confirm'),
]
