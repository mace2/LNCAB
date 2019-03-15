from django.contrib import admin
from .models import Game, Tournament,Day,Venue
# Register your models here.


class VenueAdmin(admin.ModelAdmin):
    pass


admin.site.register(Venue, VenueAdmin)


class DayAdmin(admin.ModelAdmin):
    pass


admin.site.register(Day, DayAdmin)


class GameAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game, GameAdmin)


class TournamentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tournament, TournamentAdmin)


