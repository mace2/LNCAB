from django.contrib import admin
from .models import Team, Region
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    pass


admin.site.register(Team, TeamAdmin)


class RegionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Region, RegionAdmin)
