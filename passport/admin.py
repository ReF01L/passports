from django.contrib import admin
from .models import Barsa, Profile


@admin.register(Barsa)
class BarsaAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'user_id', 'nat', 'gunlic', 'crime')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('login', 'password')
