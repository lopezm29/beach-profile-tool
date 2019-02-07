from django.urls import path
from . import views
from surveys.views import *

urlpatterns=[
    path('stations/add', views.station, name="stations"),
    path('profiles/add', views.profile, name="profiles"),
    path('surveys/add', views.survey, name="surveys"),
    path('surveys/<int:pk>/view/', views.survey_details, name='survey_details'),
    path('surveys/<int:instance_id>/edit/', views.survey_edit, name='survey_edit'),
    path('surveys<int:instance_id>/calc', views.survey_calc),
    #path('stations/', StationView.as_view()), #Edit View
    #path('stations/add', StationCreate.as_view()), #Form Made
    #path('stations/edit', StationUpdate.as_view()),
    #path('profiles/add', ProfileCreate.as_view()), #Form Made
    #path('profiles/edit', ProfileUpdate.as_view()), 
    #path('surveys/add', SurveyCreate.as_view()), #Form Made
    #path('surveys/edit', SurveyUpdate.as_view()),
    path('', views.index, name='index') #Create an index?
]