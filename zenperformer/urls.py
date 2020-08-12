"""zenperformer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from client.views import profile_match
from client.views import index
from client.views import coach_sessions
from client.views import coach_session_create
from client.views import signup
from client.views import issues
from client.views import privacy_policy
from client.views import conditions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile_match', profile_match),
    path('coach_sessions', coach_sessions),
    path('coach_session_create', coach_session_create),
    path('signup', signup),
    path('issues', issues),
    path('privacy_policy', privacy_policy),
    path('conditions', conditions),
    path('', index),


    # path('profile_match/', views.profile_match),

    # url('profile_match', views.profile_match, name='Profile Match'),
]
