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
]