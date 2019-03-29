from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

from django.views import generic
from .models import Game, Tournament, Day, Point, Foul, Win
from users.models import Player
from teams.models import Team
from django.template import loader
from django.db.models import Count, Sum


class GamesView(generic.ListView):
    template_name = 'tournaments/index.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        try:
            self.day = Day.objects.get(number=self.kwargs['day'])
        except Day.DoesNotExist:
            raise Http404()
        return self.day.game_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prev_day"] = self.day.number - 1
        context["next_day"] = self.day.number + 1
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

    def get_context_data(self, **kwargs):
        tournament = Tournament.objects.get(id=self.kwargs['tournament'])
        context = super().get_context_data(**kwargs)
        context["standings"] = Win.objects.filter(tournament=tournament).values('team__name').annotate(wins=Count('team'))
        context["point_leaders"] = Point.objects.filter(game__day__tournament=tournament)\
            .values('player__team__name').annotate(points=Sum('value'))
        context["foul_leaders"] = Foul.objects.filter(game__day__tournament=tournament)\
            .values('player__team__name').annotate(fouls=Count('game'))
        return context
