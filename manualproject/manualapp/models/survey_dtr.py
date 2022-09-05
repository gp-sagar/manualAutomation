from typing import List, Optional
from django.db import models


class MicrogridSurveydtr(models.Model):
    project_name = models.CharField(max_length=50)
    substation_name = models.CharField(max_length=50)
    feeder_name = models.CharField(max_length=50)
    feeder_code = models.CharField(max_length=50)
    location_number = models.CharField(max_length=50)
    ss_code = models.CharField(max_length=50)
    dtr_name = models.CharField(max_length=50)
    dtr_code = models.CharField(max_length=50)
    dtr_capacity = models.CharField(max_length=10)
    dtr_make = models.CharField(max_length=50)
    phase = models.CharField(max_length=5)
    earthing = models.CharField(max_length=5)
    oil_leakage = models.CharField(max_length=5)
    dt_mount_structure = models.CharField(max_length=50)
    mount_structure_condition = models.CharField(max_length=10)
    conn_type = models.CharField(max_length=20)
    dt_ht_available = models.CharField(max_length=5)
    dt_condition = models.CharField(max_length=20)
    dt_sr_no = models.CharField(max_length=20)
    dt_meter_make = models.CharField(max_length=50, blank=True, null=True)
    power_factor = models.CharField(max_length=20)
    remarks = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    site_id = models.CharField(
        unique=True, max_length=100, blank=True, null=True)
    transformer_id = models.CharField(
        unique=True, max_length=200, blank=True, null=True)
    dtr_model = models.CharField(max_length=30)
    dtr_mount = models.CharField(max_length=30)
    dt_meter_available = models.CharField(max_length=50)
    dt_meter_connected = models.CharField(max_length=50)
    dt_meter_serial_number = models.CharField(max_length=50)
    dt_meter_type = models.CharField(max_length=50)
    dt_meter_status = models.CharField(max_length=50)
    notes = models.CharField(max_length=500, blank=True, null=True)
    feeder_id = models.CharField(max_length=200, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    qc_time = models.CharField(max_length=45, blank=True, null=True)
    qc_status = models.CharField(max_length=45, blank=True, null=True)
    user = models.CharField(max_length=45, blank=True, null=True)
    # Field name made lowercase.
    imagescount = models.IntegerField(
        db_column='imagesCount', blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    resurvey_status = models.CharField(max_length=10, blank=True, null=True)
    ct_factor = models.FloatField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    energy_ct_factor = models.FloatField(blank=True, null=True)
    active_power_ct_factor = models.FloatField(blank=True, null=True)
    current_ct_factor = models.FloatField(blank=True, null=True)
    json_ct_factors = models.TextField(blank=True, null=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    is_postpaid_site = models.IntegerField(blank=True, null=True)
    is_service_charge_enabled = models.IntegerField(blank=True, null=True)
    is_real_estate = models.IntegerField(blank=True, null=True)
    is_kvah_billing = models.IntegerField(blank=True, null=True)
    real_estate_project = models.CharField(
        max_length=45, blank=True, null=True)
    is_online_payment_allowed = models.IntegerField(blank=True, null=True)

    @staticmethod
    def get_site_list(site_ids: Optional[List[str]] = None):
        if site_ids:
            return MicrogridSurveydtr.objects.filter(site_id__in=site_ids).values('site_id', 'site_name')
        return MicrogridSurveydtr.objects.all().values('site_id', 'site_name')

    class Meta:
        managed = False
        db_table = 'microgrid_surveydtr'
        unique_together = (('transformer_id', 'dtr_code'),)
