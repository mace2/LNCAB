from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

from django.views import generic
from .models import Game, Tournament, Day, Point, Foul
from users.models import Player
from teams.models import Team


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
        context = super().get_context_data(**kwargs)
        context["local_points"] = Point.objects.filter(
            player__team=self.kwargs['game'].team_local,
            game=self.kwargs['game']
        )
        context["visitor_points"] = Point.objects.filter(
            player__team=self.kwargs['game'].team_visitor,
            game=self.kwargs['game']
        )

        context["local_fouls"] = Foul.objects.filter(
            player__team=self.kwargs['game'].team_local,
            game=self.kwargs['game']
        )
        context["visitor_fouls"] = Foul.objects.filter(
            player__team=self.kwargs['game'].team_visitor,
            game=self.kwargs['game']
        )

        return context


