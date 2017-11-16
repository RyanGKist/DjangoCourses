from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$' , views.index),
	url(r'^courseAdd$', views.course_create),
	url(r'^remove(?P<uid>\d+)$', views.destroy),
	url(r'^destroy(?P<uid>\d+)$', views.destroy_data)
]