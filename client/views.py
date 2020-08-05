from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import pandas as pd
import numpy as np

import itertools as it
# import matplotlib.pyplot as plt
from itertools import combinations
import random


import json

from .models import Client
from .models import Coach_sessions


def index(request):
    context = {'a': 'Hi there'}
    return render(request, 'index.html', context)


def profile_match(request):
    obj = Client.objects.get(id=1)
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

# def profile_match(request, *args, **kwargs):
# if request.method == 'POST':
#     print(request.POST.dict())
#     request.POST.get('yr')

# skills = ['Racism', 'Divorce', 'Mental Abuse', 'Physical Abuse', 'Drug Addiction',
#           'Alcohol Addiction', 'Stress', 'Depression', 'Unemployment']  # 9 skills
# city = ['New York City', 'Los Angeles', 'San Francisco', 'Washington DC',
#         'Las Vegas', 'Miami', 'Phoenix', 'Chicago', 'Boston', 'Houston']  # 10 cities
# comb, skills_com = [], []
# for i in range(1, len(skills)+1):
#     com = [list(x) for x in combinations(skills, i)]
#     comb.append(com)

# for i in comb:
#     for j in i:
#         skills_com.append(tuple(j))

# data = []
# dict = {'exp': '0', 'skills': '0', 'city': '0'}

# for dicts in list(range(0, 1000)):
#     data.append(dict.copy())

# for i in data:
#     i['exp'] = int(random.choice(exp))
#     i['skills'] = random.choice(skills_com)
#     i['city'] = random.choice(city)
# context = {
#     'exp': [1, 2, 3, 4, 5, 6, 7],

#     'skills': skills,
#     'city': city,
# }

# return render(request, 'profile_match.html', context)
