from dataclasses import field, fields
from pyexpat import model
from django import forms
from .survey_dtr import MicrogridSurveydtr
from .survey_feeder import MicrogridSurveyfeeder
from .portal_auth_user import PortalAuthUser

class siteform(forms.ModelForm):
    class Meta:
        model = MicrogridSurveydtr
        fields = ('site_name',)
        
class FeederForm(forms.ModelForm):
    class Meta:
        model = MicrogridSurveydtr
        fields = ('feeder_id',)

class HesForm(forms.ModelForm):
    class Meta:
        model = PortalAuthUser
        fields = ('username',)
        