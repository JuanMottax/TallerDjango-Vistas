from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_one_measurement
from .logic.logic_measurements import delete_one_measurement
from django.http import HttpResponse 
from django.core import serializers


def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type = 'application/json')
    
def get_measurement(request):
    measurement = get_one_measurement()
    measurement_list = serializers.serialize('json', measurement)
    return HttpResponse(measurement_list, content_type = 'application/json')

def delete_measurement(request):
    measurement = delete_one_measurement()
    measurement_list = serializers.serialize('json', measurement)
    return HttpResponse(measurement_list, content_type = 'application/json')
# Create your views here.
