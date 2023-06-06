from django.contrib import admin
from . models import album
from .models import Team

# Register your models here.

admin.site.register(album)
admin.site.register(Team)
