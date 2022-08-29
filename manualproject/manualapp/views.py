from django.shortcuts import render
from django.http import JsonResponse
from .models import MicrogridSurveydtr
from .models import MicrogridSurveyhouseholdinfo
from .models.connection import my_custom_sql
from django.http import HttpResponse, Http404
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def hesAccess(request):
    return render(request, 'hesaccess.html')

def meterDetails(request):
    return render(request, 'meterDetails.html')

def propertyMeter(request, site):
    meter_lis_data = list(MicrogridSurveyhouseholdinfo.get_meter_list(site))
    return  JsonResponse({'sites':meter_lis_data})

# get site_id and site_name
def propertySites(request):
    params = request.GET.get('site')
    if params:
        params = params.split(',')
    # TODO: validate the data
    site_lis_data = list(MicrogridSurveydtr.get_site_list(params))
    return  JsonResponse({'sites':site_lis_data})

# get site_name, property type, site_id, feeder_id
def get_json_data(request):
    # TODO: Validate Input params
    site_id = request.GET.get('property')
    meter = request.GET.get('meter')
    if not all([site_id, meter]):
        return JsonResponse({"message": "Site and meter are required."}, safe=False, status=400)
    query = """
    Select 
        sdtr.site_name, is_real_estate, sshi.grid_id, sc_no, msf.feeder_name
    from 
        microgrid_surveyhouseholdinfo as sshi
    inner join 
        microgrid_surveydtr as sdtr on sshi.site_id = sdtr.site_id
    inner join 
        dcu_info as di on sshi.site_id = di.site_id
    inner join 
        microgrid_surveyfeeder as msf on di.feeder_id = msf.feeder_id
    where
        sshi.site_id =  %(site_id)s
    and 
        meter_serial =  %(meter)s
    """
    datas = my_custom_sql(query, {'site_id':site_id, 'meter': meter}, fetchone=True)

    if not datas:
        return JsonResponse({"message": "Item Not Found"}, safe=False, status=404)
    return JsonResponse(datas, safe=False)

# get Hes Username
def hes_username(request):
    site_id = request.GET.get('property')
    query = """
    select 
        username 
    from 
        auth_user
    where 
        dtr_list = %(site_id)s;
    """
    
    site_id = my_custom_sql(query, {'site_id':site_id}, db_name='db_portal', fetchone=True)

    if not site_id:
        return JsonResponse({"message": "Item Not Found"}, safe=False, status=404)
    return JsonResponse(site_id, safe=False)


    

