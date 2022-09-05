from django.db import models

class MicrogridSurveyhouseholdinfo(models.Model):
    site_name = models.CharField(max_length=100)
    name_bill = models.CharField(max_length=50)
    name_tenant = models.CharField(max_length=50)
    sc_no = models.CharField(unique=True, max_length=100)
    contact_bill = models.CharField(max_length=20)
    contact_tenant = models.CharField(max_length=20)
    email_bill = models.CharField(max_length=50)
    email_tenant = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    supply_hrs = models.CharField(max_length=10)
    meter_serial = models.CharField(max_length=50)
    meter_make = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    meter_type = models.CharField(max_length=20)
    working_status = models.CharField(max_length=50)
    meter_reading_kwh = models.CharField(max_length=20)
    meter_reading_kvah = models.CharField(max_length=20)
    meter_reading_md = models.CharField(max_length=20)
    supply_type = models.CharField(max_length=20)
    tariff = models.CharField(max_length=10)
    ci_status = models.CharField(max_length=20)
    connection_status = models.CharField(max_length=20)
    surveyor_name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    startlat = models.FloatField(db_column='startLat')  # Field name made lowercase.
    startlng = models.FloatField(db_column='startLng')  # Field name made lowercase.
    connection_category = models.CharField(max_length=20)
    establishment = models.CharField(max_length=50)
    pole_no = models.CharField(max_length=20)
    dt_code = models.CharField(max_length=20)
    id_proof_type_bill = models.CharField(max_length=20)
    id_proof_no_bill = models.CharField(max_length=20)
    id_proof_type_tenant = models.CharField(max_length=20)
    id_proof_no_tenant = models.CharField(max_length=20)
    consumer_category = models.CharField(max_length=50)
    department_name = models.CharField(max_length=50)
    enclosure = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    approachability = models.CharField(max_length=50)
    height_meter = models.CharField(max_length=50)
    connection_type = models.CharField(max_length=50)
    cable_type = models.CharField(max_length=50)
    payment_mode = models.CharField(max_length=50)
    problems = models.CharField(max_length=500)
    grid_id = models.CharField(max_length=50)
    meter_address = models.CharField(max_length=50)
    site_id = models.CharField(max_length=100, blank=True, null=True)
    pole_id = models.CharField(max_length=100, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    house_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    father_name_bill = models.CharField(max_length=50)
    sc_no_new_final = models.CharField(max_length=100, blank=True, null=True)
    meter_bc_number = models.CharField(max_length=30)
    meter_location = models.CharField(max_length=50)
    contracted_demand = models.CharField(max_length=30)
    kwh_reading = models.CharField(max_length=30)
    time = models.DateTimeField(blank=True, null=True)
    qc_status = models.CharField(max_length=100, blank=True, null=True)
    qc_time = models.CharField(max_length=45, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    imagecount = models.IntegerField(db_column='imageCount', blank=True, null=True)  # Field name made lowercase.
    qc_notes = models.CharField(max_length=500, blank=True, null=True)
    supervisorname = models.CharField(db_column='supervisorName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    supervisorqcstatus = models.CharField(db_column='supervisorQCStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    supervisornotes = models.CharField(db_column='supervisorNotes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    assert_seq = models.CharField(max_length=200, blank=True, null=True)
    resurvey_time = models.DateTimeField(blank=True, null=True)
    tariff_category = models.CharField(max_length=45, blank=True, null=True)
    tariff_subcategory = models.CharField(max_length=45, blank=True, null=True)
    replace_time = models.DateTimeField(blank=True, null=True)
    phase = models.CharField(max_length=1, blank=True, null=True)
    meter_category = models.CharField(max_length=10, blank=True, null=True)
    meter_replace_date = models.DateTimeField(blank=True, null=True)
    old_meter_serial = models.CharField(max_length=50, blank=True, null=True)
    meter_pp_box = models.CharField(max_length=45, blank=True, null=True)
    used_service_cable = models.CharField(max_length=45, blank=True, null=True)
    mcr_no = models.CharField(max_length=45, blank=True, null=True)
    meter_mode = models.CharField(max_length=20, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    contracted_demand_unit = models.CharField(max_length=5, blank=True, null=True)
    meter_sw_version = models.CharField(max_length=10, blank=True, null=True)
    metersoftwareversion = models.CharField(db_column='meterSoftwareVersion', max_length=60, blank=True, null=True)  # Field name made lowercase.
    meter_mapping = models.CharField(max_length=50, blank=True, null=True)
    ct_ratio = models.IntegerField(blank=True, null=True)
    meteringstatus = models.CharField(db_column='meteringStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.
    net_metering = models.IntegerField(blank=True, null=True)
    survey_stage_name = models.CharField(max_length=100, blank=True, null=True)
    meter_protocol_type = models.CharField(max_length=50, blank=True, null=True)
    
    @staticmethod
    def get_meter_list(site_id: str):
        return (
            MicrogridSurveyhouseholdinfo.objects
            .filter(site_id=site_id,)
            .exclude(meter_serial="", meter_mapping="", meter_address="")
            .values('meter_serial', 'meter_mapping', 'meter_address')
        )
        
    @staticmethod
    def get_property_meter(site_id: str):
         return (
             MicrogridSurveyhouseholdinfo.objects.filter
             (site_id=site_id, meter_serial=meter )
             .values('site_name', 'meter_serial', 'grid_id', 'site_id' )
             .first()
         )
        

    class Meta:
        managed = False
        db_table = 'microgrid_surveyhouseholdinfo'