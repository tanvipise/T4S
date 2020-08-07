from django.contrib import admin

# Register your models here.
from .models import Client
from .models import Coach_sessions, User_signup


admin.site.register(Client)
admin.site.register(Coach_sessions)
admin.site.register(User_signup)
