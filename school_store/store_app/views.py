from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Department, Course, Material

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Logged in Successfully')
            return redirect('store_app:welcome')
        else:
            messages.info(request, 'Incorrect Username or Password')
            return redirect('store_app:login')

    return render(request, 'login.html')


def welcome(request):
    return render(request, 'welcome.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('store_app:registration')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request,'Registered Successfully \n Please Login')
                return redirect('store_app:login')
        else:
            messages.info(request, 'Please check your password')
            return redirect('store_app:registration')

    return render(request, 'registration.html')


def form(request):
    return render(request, 'form.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


