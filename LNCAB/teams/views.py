from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

from django.views import generic
from tournaments.models import Game, Tournament, Day, Point, Foul, Win
from users.models import Player
from teams.models import Team, Region
from django.template import loader
from django.db.models import Count, Sum


class TeamView(generic.DetailView):
    template_name =  "teams/team.html"
    model = Team

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = Team.objects.get(id=self.kwargs["pk"])
        context["player_list"] = Player.objects.filter(team=team)
        return context
