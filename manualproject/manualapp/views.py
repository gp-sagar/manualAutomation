from django.shortcuts import render
from django.http import JsonResponse
from .models import MicrogridSurveydtr
from .models import MicrogridSurveyhouseholdinfo
import json

# Create your views here.

def index(request):
    site_lis_data = MicrogridSurveydtr.get_site_list()
    return render(request, 'index.html', {'sites':site_lis_data})

def hesAccess(request):
    return render(request, 'hesaccess.html')

def meterDetails(request):
    return render(request, 'meterDetails.html')

def propertyMeter(request, site):
    meter_lis_data = list(MicrogridSurveyhouseholdinfo.get_meter_list(site))
    return  JsonResponse({'sites':meter_lis_data})

def propertySites(request):
    params = request.GET.get('site')
    if params:
        params = params.split(',')
    # TODO: validate the data
    site_lis_data = list(MicrogridSurveydtr.get_site_list(params))
    return  JsonResponse({'sites':site_lis_data})