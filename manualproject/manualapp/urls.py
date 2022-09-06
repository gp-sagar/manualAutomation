from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('hesAccess/', views.hesAccess, name='hesAccess'),
    path('meterDetails/', views.meterDetails, name='meterDetails'),
    path('property-meter/<str:site>/', views.propertyMeter, name='propertyMeter'),
    path('property-sites/', views.propertySites, name='propertySites'),
    path('get_json_data/', views.get_json_data, name='get_json_data'),
    path('hes_username/', views.hes_username, name='hes_username'),
    path('hes_access/', views.hes_access, name='hes_access'),
    path('siteupdate/<str:site_id>', views.siteupdate, name='siteupdate'),
    path('update_site_name/<str:site_id>', views.update_site_name, name='update_site_name'),
    path('update_hes_access/', views.update_hes_access, name='update_hes_access'),
    path('editfeeder/', views.editfeeder, name='editfeeder'),
    path('feeder-list/', views.feederlist, name='feederlist'),
    path('update_feeder_name/<str:site_id>', views.update_feeder_name, name='update_feeder_name'),
]
