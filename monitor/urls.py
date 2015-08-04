#-*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.core.urlresolvers import reverse

from .views import *

urlpatterns = [
	url('^', include('django.contrib.auth.urls')),
	url(r'^$', index, name='index'),
	url(r'^reload_display/$', reload_display, name='reload_display'),
	url(r'^specs/$', specs, name='specs'),
	url(r'^setting_cp/$', setting_cp, name='setting_cp'),
	url(r'^show_database/$', show_database, name='show_db'),
	url(r'^set_cp/$', set_cp, name='set_cp'),
	url(r'^page_request/$', page_request, name='page_request'),
	url(r'^toggle_switch/$', toggle_switch, name='toggle_switch'),
	url(r'^floor_change/$', floor_change, name='floor_change'),
	url(r'^change_ciuonhp/$', change_ciuonhp, name='change_ciuonhp'),
	# Nav bar
	# 동작설정
	url(r'^setting_mode/$', setting_mode, name='setting_mode'),
	url(r'^setting_mode_confirm/$', setting_mode_confirm, name='setting_mode_confirm'),
	url(r'^operation_control/$', operation_control, name='operation_control'),
	# DB 검색
	url(r'^show_database/$', show_database, name='show_database'),
	url(r'^search_db_ciu/$', search_db_ciu, name='search_db_ciu'),
	url(r'^search_db_ciu_result/$', search_db_ciu_result, name='search_db_ciu_result'),
]
