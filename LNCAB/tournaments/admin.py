from django.contrib import admin
from .models import Game, Tournament, Day, Venue, Foul, Point, Win
# Register your models here.


class FoulInline(admin.TabularInline):
    model = Foul
    extra = 0


class PointInline(admin.TabularInline):
    model = Point
    extra = 0


class VenueAdmin(admin.ModelAdmin):
    pass


admin.site.register(Venue, VenueAdmin)


class DayAdmin(admin.ModelAdmin):
    pass


admin.site.register(Day, DayAdmin)


class GameAdmin(admin.ModelAdmin):
    inlines = (FoulInline, PointInline)


admin.site.register(Game, GameAdmin)


class TournamentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tournament, TournamentAdmin)

admin.site.register(Win)
