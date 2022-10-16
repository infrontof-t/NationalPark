from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from parkapp.models import *
from locationApp.models import *


def home(request):
    region = Region.objects.all()
    context  = {
        'region' : region
    }
    return render(request, 'home.html', context)

def region(request, id):
    region = Region.objects.get(id = id)
    park_list = Park.objects.filter(region_id = id)
    data = Region.objects.get(id = id)
    context  = {
        'region' : region,
        'pList' : park_list,
        'state' : data,
    }
    return render(request, 'region.html', context)

def park(request, id):
    # if id is None:
    #     return HttpResponseRedirect('park/park_list')
    park = Park.objects.get(id = id)
    context  = {
        'park' : park
    }
    return render(request, 'park.html', context)

def park_list(request):
    park = Park.objects.all()
    context  = {
        'park' : park
    }
    return render(request, 'park_list.html', context)