from django.contrib import admin
from .models import Game, Tournament,Jornada,Cede
# Register your models here.
class CedeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cede, CedeAdmin)

class JornadaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Jornada, JornadaAdmin)

class GameAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game, GameAdmin)


class TournamentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tournament, TournamentAdmin)


