from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


import itertools as it
# import matplotlib.pyplot as plt
from itertools import combinations
import random


import json

from .models import Client
from .models import Coach_sessions, User_signup

from .forms import CoachSessionForm, UserSignupForm

def index(request):
    return render(request, 'index.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def conditions(request):
    return render(request, 'conditions.html')

def issues(request):
    context = {'a': 'Hi there'}
    return render(request, 'issues.html', context)

def profile_match(request):
    obj = Client.objects.all().order_by('-id')[:5]    
    context = {
        'object': obj
    }
    return render(request, 'profile_match.html', context)


def coach_sessions(request):
    obj = Coach_sessions.objects.get(id=1)
    context = {
        'object': obj

    }

    return render(request, 'coach_sessions.html', context)


def coach_session_create(request):
    form = CoachSessionForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)

    context = {
        'form': form
    }

    return render(request, 'coach_session_create.html', context)


def signup(request):
    form = UserSignupForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)


def login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)

