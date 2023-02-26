from django.shortcuts import render, redirect
from backend.views import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from backend.forms import *

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def homepage(request):
    context = {
        'user': request.user,
        'username': request.user.username,
    }
    return render(request, 'homepage.html', context)

def edit_profile(request):
    return render(request, 'edit_profile.html')


def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('frontend:landing')


