from django.shortcuts import redirect, render
from django.http import JsonResponse,HttpResponseRedirect
from django.forms.models import model_to_dict
from locationApp.forms import testForm,stateForm
import math

from locationApp.models import *


def distance(lat1, lng1, lat2, lng2) :
    theta = lng1 - lng2
    dist1 = math.sin(deg2rad(lat1)) * math.sin(deg2rad(lat2))
    dist2 = math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2))
    dist2 = dist2* math.cos(deg2rad(theta))
    dist = dist1 + dist2
    dist = math.acos(dist)
    dist = rad2deg(dist) * 60 * 1.1515 * 1.609344
    return dist

def deg2rad(deg):
    return deg * math.pi / 180.0

def rad2deg(rad):
    return rad * 180.0 / math.pi

def map(request):
    data = {
        'lat':37.52,
        'lng':127.0
    }
    size = 8
    return render(request, 'locationApp/locationApp.html',{
        'state':data,
        'size':size
    })

def choice_state(request,id):
    if id is None:
        return HttpResponseRedirect('loc/map/')
    data = state.objects.get(id = id)
    size = 12
    return render(request, 'locationApp/locationApp.html',{
        'state':data,
        'size':size
    })

def state2(request):
    data = test.objects.all()
    lat = request.GET.get('park_latitude')
    lng = request.GET.get('park_longitude')
    map_list = []
    for d in data:
        d = model_to_dict(d)  
        dist = distance(float(lat), float(lng), d['park_latitude'], d['park_longitude'])
        if(dist <= 10000):  # 100km 이내의 장소만 응답결과로 저장 (10m 단위)
            map_list.append(d)
    return JsonResponse(map_list,safe=False)

def stateMain(request):
    data = state.objects.all()
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    map_list = []
    for d in data:
        d = model_to_dict(d)  
        dist = distance(float(lat), float(lng), d['lat'], d['lng'])
        if(dist <= 10000):  # 100km 이내의 장소만 응답결과로 저장 (10m 단위)
            map_list.append(d)
    return JsonResponse(map_list,safe=False)







def form_creat(request):
    if request.method == 'POST':
        form = testForm(request.POST)
        if form.is_valid():
            te = form.save(commit=False)
            te.save()
            return redirect('/loc/course/create/')
    else:
        form = testForm()
    return render(request, 'locationApp/form_model.html',
    {'form':form})

def state_creat(request):
    if request.method == 'POST':
        form = stateForm(request.POST)
        if form.is_valid():
            te = form.save(commit=False)
            te.save()
            return redirect('/loc/state/create/')
    else:
        form = stateForm()
    return render(request, 'locationApp/state_model.html',
    {'form':form})