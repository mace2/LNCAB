from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

from django.views import generic
from .models import Game, Tournament, Day, Point, Foul, Win
from users.models import Player
from teams.models import Team
from django.template import loader
from django.db.models import Count, Sum


class TournamentsView(generic.ListView):
    template_name = 'tournaments/tournaments.html'
    context_object_name = 'active_tournament_list'

    def get_queryset(self):
        try:
            self.tournaments = Tournament.objects.filter(is_active=True)
        except Tournament.DoesNotExist:
            raise Http404()
        return self.tournaments.all()

    def get_context_data(self, **kwargs):
        context = super(TournamentsView, self).get_context_data(**kwargs)
        return context


class GamesView(generic.ListView):
    template_name = 'tournaments/index.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        try:
            self.day = Day.objects.get(tournament=self.kwargs['pk'], number=self.kwargs['day'])
        except Day.DoesNotExist:
            raise Http404()
        return self.day.game_set.all().order_by("date_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prev_day"] = self.day.number - 1
        context["next_day"] = self.day.number + 1
        context["tournament"] = self.day.tournament.pk

        return context





class DetailView(generic.DetailView):
    template_name = 'tournaments/detail.html'
    model = Game

    def get_context_data(self, **kwargs):
        game = Game.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context["local_points"] = Point.objects.filter(
            player__team=game.team_local,
            game=game
        )
        context["visitor_points"] = Point.objects.filter(
            player__team=game.team_visitor,
            game=game
        )

        context["local_fouls"] = Foul.objects.filter(
            player__team=game.team_local,
            game=game
        )
        context["visitor_fouls"] = Foul.objects.filter(
            player__team=game.team_visitor,
            game=game
        )
        return context


class BracketView(generic.TemplateView):
    template_name = "tournaments/bracket.html"


class StatisticsView(generic.TemplateView):
    template_name = "tournaments/stats.html"

    class StandingsEntry:
        def __init__(self, place, team, value):
            self.place = place
            self.team = team
            self.value = value

    def get_context_data(self, **kwargs):

        try:
            tournament = Tournament.objects.get(id=self.kwargs['tournament'])
        except Tournament.DoesNotExist:
            raise Http404()

        context = super().get_context_data(**kwargs)
        curr = 0
        # last = -1

        standings = []
        point_leaders = []
        foul_leaders = []

        wins = Win.objects.filter(tournament=tournament)\
            .values('team__name').annotate(wins=Count('team')).order_by('-wins')[:10]

        no_wins = tournament.team_set.exclude(id__in=Win.objects.filter(tournament=tournament).values("team__id"))

        for entry in wins:
            # if last != entry["wins"]:
            #     curr = curr + 1
            #     last = entry["wins"]
            curr += 1
            standings.append(
                self.StandingsEntry(place=curr, team=entry["team__name"], value=entry["wins"])
            )
        for entry in no_wins:
            curr += 1
            standings.append(self.StandingsEntry(place=curr, team=entry, value=0))

        context["standings"] = standings

        # points

        points = Point.objects.filter(game__day__tournament=tournament)\
            .values('player__team__name').annotate(points=Sum('value')).order_by('-points')[:10]

        no_points = tournament.team_set.exclude(
            id__in=Point.objects.filter(game__day__tournament=tournament)
        )

        # last = -1
        curr = 0

        for entry in points:
            # if last != entry["points"]:
            #     curr = curr + 1
            #     last = entry["points"]
            curr += 1
            point_leaders.append(
                self.StandingsEntry(place=curr, team=entry["player__team__name"], value=entry["points"])
            )
        for entry in no_points:
            curr += 1
            point_leaders.append(self.StandingsEntry(place=curr, team=entry, value=0))

        context["point_leaders"] = point_leaders

        # fouls

        fouls = Foul.objects.filter(game__day__tournament=tournament)\
            .values('player__team__name').annotate(fouls=Count('game')).order_by('-fouls')[:10]

        no_fouls = context["teams_no_fouls"] = tournament.team_set.exclude(
            id__in=Foul.objects.filter(game__day__tournament=tournament)
        )

        # last = -1
        curr = 0

        for entry in fouls:
            # if last != entry["fouls"]:
            #     curr = curr + 1
            #     last = entry["fouls"]
            curr += 1
            foul_leaders.append(
                self.StandingsEntry(place=++curr, team=entry["player__team__name"], value=entry["fouls"])
            )
        for entry in no_fouls:
            curr += 1
            foul_leaders.append(self.StandingsEntry(place=curr, team=entry, value=0))

        context["foul_leaders"] = foul_leaders

        context["teams_by_state"] = Tournament.objects.get(id=1)\
            .team_set.values('state__name')\
            .annotate(number=Count('id'))\
            .order_by('-number')

        return context
