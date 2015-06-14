from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^ajax_page_request/$', views.ajax_page_request, name='page_request'),
]
