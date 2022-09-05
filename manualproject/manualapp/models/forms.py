from dataclasses import field, fields
from django import forms
from manualapp.models.survey_dtr import MicrogridSurveydtr
from manualapp.models.survey_feeder import MicrogridSurveyfeeder

class siteform(forms.ModelForm):
    class Meta:
        model = MicrogridSurveydtr
        fields = ('site_name',)
        
class FeederForm(forms.ModelForm):
    class Meta:
        model = MicrogridSurveydtr
        fields = ('feeder_id',)