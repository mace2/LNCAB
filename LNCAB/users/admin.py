from django.contrib import admin
from .models import Coach
from .models import Scorekeeper
from .models import Player

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Coach, UserAdmin)
admin.site.register(Scorekeeper, UserAdmin)
admin.site.register(Player, UserAdmin)
