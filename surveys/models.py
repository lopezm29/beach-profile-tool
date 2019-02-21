from django.db import models
from datetime import datetime
from django.forms import ModelForm

# Create your models here.dsd
class Survey(models.Model):
    instance_id = models.AutoField(primary_key=True)
    beach_name = models.CharField(max_length=200,blank=False)
    start = models.DateField(blank=False)
    mhhw = models.DecimalField(decimal_places=3, max_digits=6)
    mllw = models.DecimalField(decimal_places=3, max_digits=6)

    def __str__(self):
        return self.beach_name

class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    survey_instance = models.ForeignKey(Survey, blank=False, null=True, on_delete=models.PROTECT)
    section = models.CharField(max_length=3,blank=False)
    #number_of_stations = models.IntegerField()

    elevation_control = models.DecimalField(decimal_places=3, max_digits=5, blank=True, null=True)

    width = models.DecimalField(decimal_places=3, max_digits=8, blank=True, null=True)
    volume = models.DecimalField(decimal_places=6, max_digits=9, blank=True, null=True)
    def __str__(self):
        return str(self.survey_instance.beach_name) + " - " + self.section

class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, blank=True, on_delete=models.PROTECT)
    number = models.IntegerField(max_length=None, blank=True, null=True)
    distance = models.DecimalField(decimal_places=3, max_digits=6, blank=False, null=True)
    z = models.DecimalField(decimal_places=3, max_digits=6, blank=False, null=True)

    true_distance = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True, default=0)
    true_elevation = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True, default=0)

    comment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.profile) + ": Station " + str(self.number)

# class Reduced(models.Model):
#     id = models.AutoField(primary_key=True)
#     station = models.ForeignKey(Station, on_delete=models.PROTECT, blank=False)

#     true_distance = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
#     true_elevation = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
