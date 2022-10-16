from django.shortcuts import redirect, render
from django.http import JsonResponse,HttpResponseRedirect
from django.forms.models import model_to_dict
from locationApp.forms import testForm,stateForm
import math


from locationApp.models import *



def getState(request):
    data = test.objects.all()

    map_list = []
    for d in data:
        # 모델에서 받아온 데이터를 dictionary 화
        d = model_to_dict(d)  
        # 배열에 저장
        map_list.append(d)
    # json으로 넘겨줌
    return JsonResponse(map_list,safe=False)




def showMap(request):
    park =  test.objects.get(id=2)
    latlng = {
        "lat": park.park_latitude,
        "lng": park.park_longitude
    }
    print(park.park_latitude)
    return render(request, 'locationApp/locationApp copy 2.html',latlng)
    

def showFacility(request,id):
    park =  test.objects.get(id=id)
    latlng = {
        "lat": park.park_latitude,
        "lng": park.park_longitude
    }
    print(park.park_latitude)
    return render(request, 'locationApp/facility.html',latlng)
