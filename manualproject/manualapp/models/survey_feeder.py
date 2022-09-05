from typing import List, Optional
from django.db import models
from .models import MicrogridSurveypss

class MicrogridSurveyfeeder(models.Model):
    feeder_id = models.CharField(unique=True, max_length=100)
    pss = models.ForeignKey(MicrogridSurveypss, models.DO_NOTHING)
    feeder_name = models.CharField(max_length=100)
    rated_capacity = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    feeder_code = models.CharField(max_length=30, blank=True, null=True)
    time_old = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    
    @staticmethod
    def get_feeder_list(feeder_id: Optional[List[str]] = None):
        if feeder_id:
            return MicrogridSurveyfeeder.objects.filter(feeder_id__in=feeder_id).values('feeder_id', 'feeder_name')
        return MicrogridSurveyfeeder.objects.all().values('feeder_id', 'feeder_name')
    
    class Meta:
        managed = False
        db_table = 'microgrid_surveyfeeder'