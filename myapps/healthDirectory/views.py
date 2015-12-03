from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render,render_to_response
from .models import Service_provider
import cgi
import os
import json
from django.conf import settings
from django.template import RequestContext, loader
from django.db.models import Q

def index(request):
        return render(request, 'healthDirectory/homepage.html')
        #return render(request, 'healthDirectory/regis-login.html')
	#return render(request, 'healthDirectory/regis-login.html')

def regislogin(request):
	return render(request, 'healthDirectory/regis-login.html')

def validate(request):
	"""return HttpResponse("Hello, world. You're at the polls index.")"""
	ser_name = request.GET.get('ser_name')
	ser_spl = request.GET.get('ser_spl')
	ser_location=request.GET.get('ser_location')
	ser_phNum=request.GET.get('ser_phNum')
	ser_psword=request.GET.get('ser_psword')
	ser_addr=request.GET.get('ser_addr')
	ser_email=request.GET.get('ser_email')
	response = {}
	if not Service_provider.objects.filter(ser_email=ser_email):
		s = Service_provider(ser_name=ser_name,ser_phNum=ser_phNum,ser_spl=ser_spl,ser_psword=ser_psword,ser_location=ser_location,ser_addr=ser_addr,ser_email=ser_email)
		s.save()
		response['status'] = 'sucess'
	else:
		response['status'] = 'failure'
	json_data = json.dumps(response)
	return HttpResponse(json_data, content_type = "application/json")


def validatelogin(request):
	ser_email=request.POST.get('ser1_email')
	ser_psword=request.POST.get('ser1_psword')
	if Service_provider.objects.filter(ser_email=ser_email,ser_psword=ser_psword):
		ser=Service_provider.objects.filter(ser_email=ser_email,ser_psword=ser_psword)
		template = loader.get_template('healthDirectory/login.html')
		context = RequestContext(request, {
			'ser': ser,
		})
		return HttpResponse(template.render(context))
	else:
		return render_to_response('healthDirectory/regis-login.html')

def searchresults(request) :
		ser_value=request.POST.get('searchvalue')
		#ser=Service_provider.objects.filter(ser_name=ser_value)
		ser = Service_provider.objects.filter(Q(ser_name__icontains=ser_value) | Q(ser_spl__icontains=ser_value) | Q(ser_location__icontains=ser_value))
		# ser = Service_provider.objects.filter(ser_spl__icontains=ser_value)
		# ser = Service_provider.objects.filter(ser_location__icontains=ser_value)
		# ser=Service_provider.objects.filter(Q(ser_name__startswith=ser_value))
		template = loader.get_template('healthDirectory/results.html')
		context = RequestContext(request, {
		        'ser': ser,
		})
		return HttpResponse(template.render(context))
		#return render(request, 'healthDirectory/results.html')

def editprofile(request):
		ser_email=request.POST.get('seremail')
		ser=Service_provider.objects.filter(ser_email=ser_email)
		template = loader.get_template('healthDirectory/editpage.html')
		context = RequestContext(request, {
			'ser': ser,
		})
		return HttpResponse(template.render(context))

def updateprofile(request):
		ser_name = request.POST.get('ser_name')
		ser_spl = request.POST.get('ser_spl')
		ser_location=request.POST.get('ser_location')
		ser_phNum=request.POST.get('ser_phNum')
		ser_psword=request.GET.get('ser_psword')
		ser_cpsword=request.GET.get('ser_cpsword')
		ser_addr=request.POST.get('ser_addr')
<<<<<<< HEAD
		ser_email=str(request.POST.get('ser_email'))
=======
		ser_email=request.POST.get('ser_email','')
>>>>>>> 25b5e4f430ea3a2d9aaeefd848c05359f34f08cb
		response = {}
	
		if not ser_cpsword==ser_psword:
			response = 'Enter the password again'
			return HttpResponse(response)
		if ser_email:
			if ser_name:
				Service_provider.objects.filter(ser_email=ser_email).update(ser_name=ser_name) 
			if ser_spl:
				Service_provider.objects.filter(ser_email=ser_email).update(ser_spl=ser_spl)
			if ser_location:
				Service_provider.objects.filter(ser_email=ser_email).update(ser_location=ser_location)
			if ser_phNum:
				Service_provider.objects.filter(ser_email=ser_email).update(ser_phNum=ser_phNum)
			if ser_psword:
				Service_provider.objects.filter(ser_email=ser_email).update(ser_psword=ser_psword)
			if ser_addr:
				Service_provider.objects.filter(ser_email=ser_email).update(ser_addr=ser_addr)
						
		
		ser=Service_provider.objects.filter(ser_email=ser_email)
		template = loader.get_template('healthDirectory/login.html')
		context = RequestContext(request, {
			'ser': ser,
		})
		return HttpResponse(template.render(context))
		# ser=Service_provider.objects.filter(ser_email=ser_email)
		# return HttpResponse(ser)
		
		
			
		#Service_provider.objects.filter(ser_email=ser_email).update(ser_name=ser_name) 
		#ser_email=ser_email+''
		# ser = Service_provider.objects.filter(ser_email= ser_email)
		#s.ser_email = ser_email
		#s.save()
		#ser=Service_provider.objects.filter(ser_email='ser_email')
		# return render(request,"healthDirectory/login.html",{'ser':ser})
		# return HttpResponse(s)