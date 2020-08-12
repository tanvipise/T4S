from itertools import islice
from django.shortcuts import render
from django.http import HttpResponse
# from itertools import islice
# from on.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

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
    queryset = Client.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'profile_match.html', context)


def coach_sessions(request):
    queryset = Coach_sessions.objects.all()
    context = {
        'object': queryset,
    }

    return render(request, 'coach_sessions.html', context)


def coach_session_create(request):
    # does the validation as well for the form
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


# def coach(jobs1, pref):

#     jobs1['words'] = jobs1.Expertise.str.strip().str.split('[\W_]+')

#     vectorizer = TfidfVectorizer(
#         tokenizer=lambda doc: doc, lowercase=False, stop_words='english', use_idf=True, norm='l1')
#     Y = vectorizer.fit_transform(jobs1['words'])

#     Y = pd.DataFrame(Y.toarray(), columns=vectorizer.get_feature_names())

#     skills = pref[0]

#     X = vectorizer.transform(skills)

#     X = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
#     # print(X)

#     similarity = (cosine_similarity(X, Y))
#     similarity.shape
#     # print(similarity)

#     def find_similar(tfidf_matrix, index, top_n):
#         cosine_similarities = cosine_similarity(Y, tfidf_matrix).flatten()
#         related_docs_indices = [i for i in cosine_similarities.argsort()[
#             ::-1] if i != index]
#         return [(index, cosine_similarities[index]) for index in related_docs_indices][0:top_n]

#     num = 10
#     rec_jobs = find_similar(X, 1, num)

#     a = []
#     for i in range(0, num):
#         mn = rec_jobs[i][0] % len(jobs1)
#         a.append(jobs.loc[mn].tolist())
#     # print(a)

#     Output = []
#     for i in range(len(a)):
#         Output.append([a[i][0], a[i][1]])
#     # print(Output)

#     def Sort(sub_li):
#         sub_li.sort(key=lambda x: x[1], reverse=True)
#         return sub_li
#     Sort(Output)

#     # print(Sort(Output))

#     OutputAdd = []
#     for i in range(len(a)):
#         OutputAdd.append([a[i][0], a[i][2]])

#     LocSorted = []
#     for z in range(len(OutputAdd)):
#         if OutputAdd[z][1] == pref[2]:
#             LocSorted.append(OutputAdd[z])

#     Outputfin = []
#     for z in range(len(LocSorted)):
#         if Output[z][0] == LocSorted[z][0]:
#             Outputfin.append([Output[z][0], Output[z][1], LocSorted[z][1]])

#     Final_Rec = []
#     for m in range(len(a)):
#         for n in range(len(Outputfin)):
#             if a[m][0] == Outputfin[n][0]:
#                 Final_Rec.append([a[m][0], a[m][1], a[m][2], a[m][3]])

#     return Final_Rec


# pref = [['Homophobia', 'Divorce'], 3, 'East Coast']
# coach(jobs, pref)
