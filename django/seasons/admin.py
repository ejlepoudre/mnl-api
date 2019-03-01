from django.contrib import admin

<<<<<<< HEAD
from .models import Season
from main.admin import mnl_admin


@admin.register(Season, site=mnl_admin)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'duration',]
=======
from .models import Season, Team


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'duration',]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name',]
>>>>>>> upstream/master
