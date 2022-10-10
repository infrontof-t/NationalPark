"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from parkapp import views
from locationApp import views
from contact import views
import config.views as views


urlpatterns = [
    path('member/', include('memberApp.urls')),
    path('admin/', admin.site.urls),
    path('', views.mainpage),

    path('park/', include('parkapp.urls')),
    path('loc/', include('locationApp.urls')),
    path('contact/', include('contact.urls')),
]
