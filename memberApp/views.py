from django.contrib.auth import authenticate, login
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Member
from django.utils import timezone
from django.http import HttpResponse


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def signup_custom(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_name = request.POST.get('user_name')

        m = Member(
            user_id=user_id, user_pw=user_pw, user_name=user_name)
        m.date_joined = timezone.now()
        m.save()

        return render(request, 'home.html')
    
        # return HttpResponse(
        #     '가입 완료<br>%s %s %s' % (user_id, user_pw, user_name))
    else:
        return render(request, 'signup.html')



        






        # form = UserForm(request.POST)
        # if form.is_valid():
        #     form.save()

        #     username = form.cleaned_data.get('username')
        #     raw_password = form.cleaned_data.get('password1')

        #     user = authenticate(username=username, password=raw_password)
        #     login(request, user)
        #     return redirect('/index')
        # else:
        #     form = UserForm()
        # return render(request, r'C:\localRepository\NationalPark\templates\signup.html', {'form': form})