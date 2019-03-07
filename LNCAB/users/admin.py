from django.contrib import admin
from .models import Coach,Team


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(Coach,UserAdmin)

class TeamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Team,TeamAdmin)
