from django.shortcuts import render
from .models import *
from .forms import *
from django.template import loader
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
# Create your views here.
def index(request):
    surveys = Survey.objects.order_by('instance_id')
    
    if 'POST' == request.method:
        return survey_details(request, request.POST['pk'])
    
    return render(request, 'surveys/index.html', {'surveys':surveys})

# class StationView(ListView):
#     model = Station

# class SurveyCreate(CreateView):
#     model = Survey
#     fields = ['beach_name', 'start', 'mhhw', 'mllw']

# class SurveyUpdate(UpdateView):
#     model = Survey
#     fields = ['beach_name', 'start', 'mhhw', 'mllw']

# class ProfileCreate(CreateView):
#     model = Profile
#     fields = ['survey_instance', 'section', 'number', 'start_of_profile', 'elevation_control']

# class ProfileUpdate(UpdateView):
#     model = Profile
#     fields = ['survey_instance', 'section', 'number', 'start_of_profile', 'elevation_control']

# class StationCreate(CreateView):
#     model = Station
#     fields = ['profile', 'number', 'northing', 'easting', 'elevation', 'comments']

# class StationUpdate(UpdateView):
#     model = Station
#     fields = ['profile', 'number', 'northing', 'easting', 'elevation', 'comments', 'distance', 'x', 'y', 'z']

def survey(request):
    form = SurveyCreate()

    if "POST" == request.method:
        form = SurveyCreate(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return profile(request)
        else:
            print('ERROR: Form invalid')

    return render(request, 'surveys/surveys.html', {'form':form})

def survey_edit(request):
    survey = get_object_or_404(Survey, instance_id=request.POST['pk'])

    if "POST" == request.method:
        form = SurveyCreate(request.POST, instance=survey)

        if form.is_valid():
            survey = form.save(commit=False)
            survey.save()
            return redirect('survey_detail')
        else:
            print('ERROR: Form invalid')

    return render(request, 'surveys/surveys.html', {'form':form})

def survey_details(request, pk=None):
    pk = request.POST['pk']
    survey = get_object_or_404(Survey, instance_id=pk)
    profile = []
    stations = []

    return render(request, 'surveys/survey_details.html', {'survey':survey})
#   if request.POST['pk']:
#        profiles = Profile.objects.filter(survey_instance=request.POST['pk'])
#        #get_list_or_404(Profile, survey_instance=request.POST['pk'])
#
#        for profile in profiles:
#            station_list = Station.objects.filter(profile_id=profile.profile_id)
#            #get_list_or_404(Station, profile_id=profile.profile_id)
#            stations.append(station_list)
#            
#    return render(request, 'surveys/survey_details.html', {'survey':survey, 'profiles':profiles, 'stations':stations})


def survey_calc(request):
    pass

def profile(request):
    form = ProfileCreate()

    if "POST" == request.method:
        form = ProfileCreate(request.POST)

        if form.is_valid():
            form.save(commit=True)

            profile = Profile.objects.latest('profile_id')
            stations = []
            for x in range(profile.number_of_stations):
                station = StationCreate(request.POST)
                if station.is_valid():
                    station.save(commit=True)
                    stations.append(station)
                else:
                    print('ERROR: Form invalid')

            return profileStationsEdit(request, stations)
        else:
            print('ERROR: Form invalid')

    return render(request, 'surveys/profiles.html', {'form':form})

def profileStationsEdit(request, stations):
    forms = []
    for station in stations:
        forms.append(get_object_or_404(Station, station_id=station.station_id))

    return render(request, 'surveys/profile_stations_edit.html', {'forms':forms})

def station(request, num_stations):

    stations = []
    for i in range(num_stations):
        stations.append(StationCreate(request.POST))

    if "POST" == request.method:
        form = StationCreate(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR: Form invalid')

    return render(request, 'surveys/stations.html', {'form':form})

def station_edit(request, profile_id):
    pass