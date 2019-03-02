from django.urls import path
from . import views
from surveys.views import *

urlpatterns=[
    path('stations/add', views.station, name="stations"),
    path('profiles/add', views.profile, name="profiles"),
    path('surveys/add', views.survey, name="surveys"),
    path('surveys/view', views.survey_details, name='survey_details'),
    path('surveys/edit', views.survey_edit, name='survey_edit'),
    path('surveys/calc', views.survey_calc, name='survey_calc'),
    path('surveys/survey_delete', views.survey_delete, name='survey_delete'),
    path('surveys/profile_delete', views.profile_delete, name='profile_delete'),
    path('surveys/station_delete', views.station_delete, name='station_delete'),
    path('surveys/delete', views.delete, name='delete'),
    path('surveys/surveys_edit', views.surveys_edit, name='surveys_edit'),
    path('surveys/profiles_edit', views.profiles_edit, name='profiles_edit'),
    path('surveys/stations_edit', views.stations_edit, name='stations_edit'),
    path('', views.index, name='index') #Create an index?
]