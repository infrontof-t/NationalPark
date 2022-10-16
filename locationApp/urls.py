from django.contrib import admin
from django.urls import path

from . import views

app_name = 'mapApp'


urlpatterns = [
 
    path('state/', views.getState , name='mountain'),
    path('map/', views.showMap , name='map'),
    path('map/facility/<int:id>', views.showFacility, name='facility'),

    
]

