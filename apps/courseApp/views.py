from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *

def index(request):
	return render(request, 'courseApp/index.html', {'Course': Course.objects.all()} )

def course_create(request):
	errors = Course.objects.basic_validations(request.POST)
	if len(errors):
		for tag , error in errors.iteritems():
			messages.error(request,error,extra_tags=tag)
			return redirect('/')
	else:
		Course.objects.create(name=request.POST['course'] , desc=request.POST['desc'])
		return redirect('/')

def destroy(request, uid):
	return render(request, 'courseApp/destroy.html', {'Course': Course.objects.get(id=uid)})

def destroy_data(request, uid):
	print uid
	b = Course.objects.get(id=uid).delete()
	return redirect('/')

# Create your views here.
