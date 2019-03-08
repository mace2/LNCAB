from django.contrib import admin
from .models import Coach


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Coach, UserAdmin)
