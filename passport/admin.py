from django.contrib import admin
from .models import Barsa


@admin.register(Barsa)
class BarsaAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'user_id', 'nat', 'gunlic', 'crime')
