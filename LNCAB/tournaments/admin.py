from django.contrib import admin
from .models import Game, Tournament
# Register your models here.


class GameAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game, GameAdmin)


class TournamentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tournament, TournamentAdmin)


