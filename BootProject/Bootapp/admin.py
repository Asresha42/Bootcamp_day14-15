from django.contrib import admin
from .models import Information


@admin.register(Information)
class Informationadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'address')