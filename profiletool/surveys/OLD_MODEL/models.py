from django.db import models
from datetime import datetime
from django.forms import ModelForm

# Create your models here.
class Survey(models.Model):
    instance_id = models.AutoField(primary_key=True)
    beach_name = models.CharField(max_length=200)
    start = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.instance_id) + " - " + self.beach_name + " " + str(self.start)

class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    survey_instance = models.ForeignKey(Survey, on_delete=models.PROTECT)
    section = models.CharField(max_length=1)
    number = models.IntegerField()
    start_of_profile = models.DateTimeField(default=datetime.now())
    elevation_control = models.DecimalField(decimal_places=3, max_digits=5, blank=True, null=True)

    def __str__(self):
        return str(self.survey_instance.beach_name) + " - " + self.section + str(self.number)

class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    number = models.IntegerField(max_length=None)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    northing = models.DecimalField(decimal_places=3, max_digits=6)
    easting = models.DecimalField(decimal_places=3, max_digits=6)
    elevation = models.DecimalField(decimal_places=3, max_digits=6)
    comments = models.CharField(max_length=200, blank=True, null=True)

    distance = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    x = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    y = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)
    z = models.DecimalField(decimal_places=3, max_digits=6, blank=True, null=True)

    def __str__(self):
        return "Station " + str(self.number)

