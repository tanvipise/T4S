from django.contrib import admin

# Register your models here.
from .models import Client
from .models import Coach_sessions


admin.site.register(Client)
admin.site.register(Coach_sessions)
