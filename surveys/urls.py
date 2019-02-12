from django.urls import path
from . import views
from surveys.views import *

urlpatterns=[
    path('stations/add', views.station, name="stations"),
    path('profiles/add', views.profile, name="profiles"),
    path('surveys/add', views.survey, name="surveys"),
    path('surveys/view/', views.survey_details, name='survey_details'),
    path('surveys/edit/', views.survey_edit, name='survey_edit'),
    path('surveys/calc/', views.survey_calc, name='survey_calc'),
    path('surveys/confirm/', views.survey_confirm, name='survey_confirm'),
    path('profile/confirm/', views.profile_confirm, name='profile_confirm'),
    path('station/confirm/', views.station_confirm, name='station_confirm'),
    path('delete', views.delete, name='delete'),
    #path('stations/', StationView.as_view()), #Edit View
    #path('stations/add', StationCreate.as_view()), #Form Made
    #path('stations/edit', StationUpdate.as_view()),
    #path('profiles/add', ProfileCreate.as_view()), #Form Made
    #path('profiles/edit', ProfileUpdate.as_view()), 
    #path('surveys/add', SurveyCreate.as_view()), #Form Made
    #path('surveys/edit', SurveyUpdate.as_view()),
    path('', views.index, name='index') #Create an index?
]