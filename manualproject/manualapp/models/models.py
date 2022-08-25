from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DcuInfo(models.Model):
    dcuid = models.CharField(db_column='dcuID', unique=True, max_length=100)  # Field name made lowercase.
    feeder_id = models.CharField(max_length=100)
    grid_id = models.CharField(unique=True, max_length=45)
    dcunetwork = models.CharField(db_column='dcuNetwork', max_length=45)  # Field name made lowercase.
    dcuchannel = models.CharField(db_column='dcuChannel', max_length=45)  # Field name made lowercase.
    dcutype = models.CharField(db_column='dcuType', max_length=45)  # Field name made lowercase.
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(blank=True, null=True)
    accuracy = models.FloatField(blank=True, null=True)
    start_time = models.DateTimeField()
    time = models.DateTimeField()
    notes = models.CharField(max_length=200, blank=True, null=True)
    imagescount = models.IntegerField(db_column='imagesCount')  # Field name made lowercase.
    site_id = models.CharField(max_length=500, blank=True, null=True)
    hw_version = models.CharField(max_length=45, blank=True, null=True)
    tariff1 = models.CharField(max_length=100, blank=True, null=True)
    dg_full_tariff = models.CharField(max_length=500, blank=True, null=True)
    tariff2 = models.CharField(max_length=100, blank=True, null=True)
    eb_full_tariff = models.CharField(max_length=500, blank=True, null=True)
    dg_meter = models.CharField(max_length=20, blank=True, null=True)
    dg_common_area_charge = models.FloatField(blank=True, null=True)
    dg_maintenance_charge = models.FloatField(blank=True, null=True)
    eb_meter = models.CharField(max_length=20, blank=True, null=True)
    eb_common_area_charge = models.FloatField(blank=True, null=True)
    eb_maintenance_charge = models.FloatField(blank=True, null=True)
    is_dual_source = models.IntegerField(blank=True, null=True)
    cmd_set_id = models.CharField(max_length=45, blank=True, null=True)
    rf_power = models.IntegerField(blank=True, null=True)
    cluster_node_limit = models.IntegerField(blank=True, null=True)
    is_meter_level_tariff = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcu_info'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MicrogridSurveyfeeder(models.Model):
    feeder_id = models.CharField(unique=True, max_length=100)
    pss = models.ForeignKey('MicrogridSurveypss', models.DO_NOTHING)
    feeder_name = models.CharField(max_length=100)
    rated_capacity = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    feeder_code = models.CharField(max_length=30, blank=True, null=True)
    time_old = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microgrid_surveyfeeder'


class MicrogridSurveypss(models.Model):
    pss_id = models.CharField(unique=True, max_length=200)
    pss_name = models.CharField(max_length=100)
    rated_capacity = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    time_old = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    vertical_mapping = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microgrid_surveypss'
