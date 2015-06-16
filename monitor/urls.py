from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^ajax_page_request/$', views.ajax_page_request, name='page_request'),
	url(r'^ajax_index_reload/$', views.ajax_index_reload, name='index_reload'),
	url(r'^ajax_set_operation_mode/$', views.ajax_set_operation_mode, name='set_operation_mode'),
]
