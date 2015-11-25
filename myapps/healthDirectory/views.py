from django.http import HttpResponse
from django.shortcuts import render
from .models import Service_provider
import cgi
import os
import json
from django.conf import settings
from django.template import RequestContext, loader


def index(request):
        return render(request, 'healthDirectory/register.html')

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
    if not Service_provider.objects.filter(ser_name=ser_name):
        s = Service_provider(ser_name=ser_name,ser_phNum=ser_phNum,ser_spl=ser_spl,ser_psword=ser_psword,ser_location=ser_location,ser_addr=ser_addr,ser_email=ser_email)
        s.save()
        response['status'] = 'sucess'
    else:
        response['status'] = 'failure'
    json_data = json.dumps(response)
    return HttpResponse(json_data, content_type = "application/json")