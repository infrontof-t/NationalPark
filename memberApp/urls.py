from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'memberApp'

urlpatterns = [
    path('login/',
        auth_views.LoginView.as_view(
            template_name=r'C:\localRepository\NationalPark\templates\login.html'
        ),
        name='login'
    ),
    path('logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path('signup/', views.signup, name='signup'),
    path('signup/custom/', views.signup_custom, name='signup_custom')
]
