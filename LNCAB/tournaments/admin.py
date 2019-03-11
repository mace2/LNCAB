from django.contrib import admin
from .models import Game, Tournament,Jornada
# Register your models here.

class JornadaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Jornada, JornadaAdmin)

class GameAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game, GameAdmin)


class TournamentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tournament, TournamentAdmin)


