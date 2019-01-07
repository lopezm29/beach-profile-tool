from django import forms
from .models import *

class SurveyCreate(forms.ModelForm):
    class Meta():
        model = Survey
        exclude = ['width']

class ProfileCreate(forms.ModelForm):
    class Meta():
        model = Profile
        exclude = ['volume', 'width']

class StationEdit(forms.ModelForm):
    class Meta():
        model = Station
        fields = '__all__'

class StationCreate(forms.ModelForm):
    class Meta():
        model = Station
        fields = '__all__'