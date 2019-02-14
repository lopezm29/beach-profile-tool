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
        return survey_details(request)
    
    return render(request, 'surveys/index.html', {'surveys':surveys})

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

def profile(request):
    form = ProfileCreate()
    pk = request.POST.get('pk')
    profiles = Profile.objects.filter(survey_instance=pk)
    latest_profile_pk = profiles.order_by('profile_id')[0].profile_id
    #get_list_or_404(Survey, survey_instance_id=request.POST.get('pk'))

    if "POST" == request.method:
        form = ProfileCreate(request.POST)

        if form.is_valid():
            form.save(commit=True)
            
            # profile = Profile.objects.order_by('profile_id')[0]
            # request.POST['profile_pk'] = profile.profile_id

            return station(request)
        else:
            print('ERROR: Form invalid')

    return render(request, 'surveys/profiles.html', {'form':form, 'pk':pk, 'profiles':profiles, 'profile_pk':latest_profile_pk})

def station(request, index=0):
    form = StationCreate()
    # num_stations = int(request.POST.get('number_of_stations'))
    pk = request.POST.get('pk')
    profile = Profile.objects.filter(profile_id=request.POST.get('profile_pk'))
    stations = Station.objects.filter(profile_id=request.POST.get('profile_pk'))
    
    if "POST" == request.method:
        i = index
        form = StationCreate(request.POST)
            
        if form.is_valid():
            form.save(commit=False)
            form.profile = request.POST.get('profile_pk')
            form.save(commit=True)
            
            return survey_details(request)
        else:
            print('ERROR: Form invalid')
        
#        if index < num_stations:
#            i = i + 1
#            return render(request, i)
#        else:
#            return survey_details(request)
    
    return render(request, 'surveys/stations.html', {'form':form, 'pk':pk, 'profile':profile, 'stations':stations})

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

def survey_details(request):
    survey = get_object_or_404(Survey, instance_id=request.POST.get('pk'))
    profiles = Profile.objects.filter(survey_instance_id=request.POST.get('pk')).order_by('section')
    profiles_stations_pair = []

    for profile in profiles:
        pair = []
        
        list_of_stations = Station.objects.filter(profile_id=profile.profile_id).order_by('number')
        
        pair.append(profile)
        pair.append(list_of_stations)
        
        profiles_stations_pair.append(pair)

    return render(request, 'surveys/survey_details.html', {'survey':survey, 'profiles_stations_pair':profiles_stations_pair})
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
#THIS NEEDS TO BE FIXED! SURVEY DELETE WOULD REROUTE TO INDEX NOT A SURVEY VIEW
def survey_delete(request):
    survey_pk = request.POST.get('pk')
    next_url = request.POST.get('next')
    
    if "POST" == request.method and "True" == request.POST.get('confirmed'):
        survey.delete()
        
        return render(request, next_url, {'pk':next_pk})
    
    elif "POST" == request.method and "False" == request.POST.get('confirmed'):
        return render(request, next_url, {'pk':next_pk})
    
    survey = get_object_or_404(Survey, instance_id=survey_pk)
    
    return render(request, 'surveys/survey_delete.html', {'survey':survey, 'pk':pk, 'next_url':next_url})

def profile_delete(request):
    profile_pk = request.POST.get('profile_pk')
    
    next_url = request.POST.get('next')
    pk = request.POST.get('pk')

    if "POST" == request.method and "True" == request.POST.get('confirmed'):
        profile = get_object_or_404(Profile, profile_id=profile_pk)
        profile.delete()
        
        return survey_detalis(request)
    
    profile = get_object_or_404(Profile, profile_id=profile_pk)

    return render(request, 'surveys/profile_delete.html', {'profile':profile, 'profile_pk':profile_pk, 'pk':pk, 'next_url':next_url})

def station_delete(request):
    station_pk = request.POST.get('station_pk')
    
    next_url = request.POST.get('next')
    pk = request.POST.get('next_pk')

    if "POST" == request.method and "True" == request.POST.get('confirmed'):
        station = get_object_or_404(Station, station_id=station_pk)
        station.delete()
        
        return survey_details(request)

    station = get_object_or_404(Station, station_id=station_pk)
    
    return render(request, 'surveys/station_delete.html', {'station':station, 'station_pk':station_pk, 'pk':pk, 'next_url':next_url})

def delete(request, confirmed_object):
    pk = request.POST.get('pk')

    if "POST" == request.method and "True" == request.POST.get('confirmed'):
        confirmed_object.delete()
        next_url = str(request.POST.get('next')) + '.html'
        next_pk = request.POST.get('next_pk')
        return render(request, next_url, {'pk':next_pk})
    elif "POST" == request.method and "False" == request.POST.get('confirmed'):
        next_url = str(request.POST.get('next')) + '.html'
        next_pk = request.POST.get('next_pk')
        return render(request, next_url, {'pk':next_pk})

    return render(request, {'pk':pk})

def survey_calc(request):
    pass

def profileStationsEdit(request, stations):
    forms = []
    for station in stations:
        forms.append(get_object_or_404(Station, station_id=station.station_id))

    return render(request, 'surveys/profile_stations_edit.html', {'forms':forms})

def station_edit(request, profile_id):
    pass