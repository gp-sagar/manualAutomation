from django.db import models

# db_portal
class PortalAuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    project_tab = models.CharField(max_length=45, blank=True, null=True)
    dtr_list = models.TextField(blank=True, null=True)
    two_way = models.CharField(max_length=200, blank=True, null=True)
    billing = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'