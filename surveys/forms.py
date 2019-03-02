from django import forms
from .models import *

class SurveyCreate(forms.ModelForm):
    class Meta():
        model = Survey
        fields = '__all__'

class ProfileCreate(forms.ModelForm):
    class Meta():
        model = Profile
        exclude = ['volume', 'width']

class StationCreate(forms.ModelForm):
    class Meta():
        model = Station
        exclude = ['true_distance', 'true_elevation']