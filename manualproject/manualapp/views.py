from dataclasses import field
from distutils.log import error
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from manualapp.models.survey_feeder import MicrogridSurveyfeeder
from .models import MicrogridSurveydtr
from .models import MicrogridSurveyhouseholdinfo
from .models.connection import my_custom_sql
from manualapp.models.forms import siteform, FeederForm
from django.contrib import messages


# def error_404(request, exception):
#         return render(request,'404error.html')

# Index Page
def index(request):
    return render(request, 'index.html')
# HES Access Page
def hesAccess(request):
    return render(request, 'hesaccess.html')
# Meter Details Page
def meterDetails(request):
    return render(request, 'meterDetails.html')
# Property Meter Json
def propertyMeter(request, site):
    meter_lis_data = list(MicrogridSurveyhouseholdinfo.get_meter_list(site))
    return JsonResponse(meter_lis_data, safe=False)
# Site Name & Site id Json
def propertySites(request):
    params = request.GET.get('site')
    if params:
        params = params.split(',')
    # TODO: validate the data
    site_lis_data = list(MicrogridSurveydtr.get_site_list(params))
    return JsonResponse({'sites': site_lis_data})
# Site Name, Property Type, Site id, Feeder id, Feeder Name, Meter Serial, Sc No, Dcu No jSON
def get_json_data(request):
    # TODO: Validate Input params
    site_id = request.GET.get('property')
    meter = request.GET.get('meter')
    meter_query = ""
    if meter is not None and meter != '':
        meter_query = " AND meter_serial = %(meter)s"
    if not any([site_id, meter]):
        return JsonResponse({"message": "Site and meter are required."}, safe=False, status=400)
    query = """
    Select 
        sdtr.site_name, sdtr.is_real_estate, sdtr.id, sdtr.site_id, sdtr.feeder_id, sshi.grid_id, sshi.sc_no, sshi.meter_serial, msf.feeder_name
    from  
        microgrid_surveydtr as sdtr 
    left join 
        microgrid_surveyfeeder as msf on sdtr.feeder_id = msf.feeder_id    
    left join 
        dcu_info as di on sdtr.site_id = di.site_id
    left join    
       microgrid_surveyhouseholdinfo as sshi on sshi.site_id =  sdtr.site_id           
    where
        sdtr.site_id = %(site_id)s
        {meter_query}
    """.format(meter_query=meter_query)
    datas = my_custom_sql(query, params=dict(
        site_id=site_id, meter=meter), fetchone=True)
    if not datas:
        return JsonResponse({"message": "Item Not Found"}, safe=False, status=404)
    return JsonResponse(datas, safe=False)

# HES Username Json
def hes_username(request):
    site_id = request.GET.get('property')
    query = """
    select 
        username 
    from 
        auth_user
    where 
        dtr_list like %(site_id)s;
    """
    site_id = my_custom_sql(
        query, {'site_id': '%' + site_id + '%'}, db_name='db_portal', fetchone=True)

    if not site_id:
        return JsonResponse({"message": "Item Not Found"}, safe=False, status=404)
    return JsonResponse(site_id, safe=False)


# HES Access Json
def hes_access(request):
    user_id = request.GET.get('username')
    query = """
    select 
        dtr_list, two_way 
    from 
        auth_user
    where 
        username = %(user_id)s;
    """
    usename_id = my_custom_sql(
        query, {'user_id': user_id}, db_name='db_portal', fetchone=True)

    if not usename_id:
        return JsonResponse({"message": "Item Not Found"}, safe=False, status=404)
    return JsonResponse(usename_id, safe=False)


# Site Name Update Page
def siteupdate(request, site_id):
    get_site = MicrogridSurveydtr.objects.get(site_id=site_id)
    return render(request, 'siteupdate.html', {'updaterecord': get_site})

# Site Name Update Logic
def update_site_name(request, site_id):
    update_site = MicrogridSurveydtr.objects.get(site_id=site_id)
    if request.method == 'POST':
        form = siteform(request.POST, instance=update_site)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated Successfully')
            return render(request, 'siteupdate.html', {'updaterecord': update_site})
        # print(form.errors)
        for field, error in form.errors.items():
            for text in error:
                messages.error(request, f'{field}: {text}')
        return render(request, 'siteupdate.html', {'updaterecord': update_site})
    form = siteform(instance=update_site)
    return render(request,  'siteupdate.html', {'form': form})

# Feeder Update Page
def editfeeder(request):
    site_id = request.GET.get('site_id', '')
    get_sites = MicrogridSurveydtr.objects.get(site_id=site_id)
    return render(request, 'editfeeder.html', {'updatefeeder': get_sites})

# Feeder id & Feeder Name Json
def feederlist(request):
    params = request.GET.get('site')
    if params:
        params = params.split(',')
    # TODO: validate the data
    feeder_lis_data = list(MicrogridSurveyfeeder.get_feeder_list(params))
    return JsonResponse({'feeder': feeder_lis_data})

def update_feeder_name(request, site_id):
    update_feeder = MicrogridSurveydtr.objects.get(site_id=site_id)
    if request.method == 'POST':
        form = FeederForm(request.POST, instance=update_feeder)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated Successfully')
            return render(request, 'editfeeder.html', {'updatefeeder': update_feeder})
        print(form.errors)
        for field, error in form.errors.items():
            for text in error:
                messages.error(request, f'{field}: {text}')
        return render(request, 'editfeeder.html', {'updatefeeder': update_feeder})
    form = FeederForm(instance=update_feeder)
    return render(request, 'editfeeder.html', {'form': form})

    
