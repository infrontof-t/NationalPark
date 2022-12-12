from django.shortcuts import redirect, render
from django.http import JsonResponse,HttpResponseRedirect
from django.forms.models import model_to_dict
from locationApp.forms import testForm,stateForm
import math


from locationApp.models import *



def getState(request):
    data = test.objects.all()
    lat = request.GET.get('park_latitude')
    lng = request.GET.get('park_longitude')
    map_list = []
    for d in data:
      # 모델에서 받아온 데이터를 dictionary화
      d = model_to_dict(d)
      dist = distance(float(lat), float(lng), d['park_latitude'], d['park_longitude'])
      if (dist <= 10000):   # 100km 이내의 장소만 응답결과로 저장(10m 단위)
        map_list.append(d)  # 배열에 저장
    # json으로 넘겨줌
    return JsonResponse(map_list, safe=False)



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
