from django.db.models.functions import Coalesce
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect

# Create your views here.
from django.db.models import Q

from django.views import generic
from .models import Game, Tournament, Day, Point, Foul, Win
from django.contrib.auth.models import User
from users.models import Player, Coach
from teams.models import Team, Region,State

from .serializers import GameSerializer
from rest_framework import viewsets

from django.db.models import Count, Sum


def get_team(user):
    if not user.is_authenticated:
        return None
    try:
        model = Coach.objects.get(user=user)
    except ObjectDoesNotExist:
        model = Player.objects.get(user=user)
    return model.team


def init_context(context, tournament, team):
    context["day"] = tournament.get_current_day().number
    context["tournament"] = tournament.pk
    if team is None:
        context["team"] = ""
        return
    context["team"] = team.pk


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


class TeamsView(generic.ListView):
    template_name = "tournaments/teams.html"
    context_object_name = "teams_list"

    def get_queryset(self):
        return Tournament.objects.get(id = self.kwargs['pk']).team_set.all()

    def get_context_data(self, **kwargs):
        tournament = Tournament.objects.get(id = self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        init_context(context, tournament, get_team(self.request.user))
        return context


class myGamesView(generic.ListView):
    template_name = "tournaments/index.html"
    context_object_name = "game_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        init_context(context, Tournament.objects.get(id=self.kwargs['pk']), get_team(self.request.user))

        return context


    def get_queryset(self):
        player_pk = self.request.user.pk
        team_id = get_team(self.request.user).id
        games = Game.objects.filter(day__tournament__id=self.kwargs["pk"])\
            .filter(Q(team_local=team_id) | Q(team_visitor=team_id))
        return games





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

        init_context(context, self.day.tournament, get_team(self.request.user))

        return context





class DetailView(generic.DetailView):
    template_name = 'tournaments/detail.html'
    model = Game

    def get_context_data(self, **kwargs):
        game = Game.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context["local_points"] = Point.objects.filter(
            player__team=game.team_local,
            quarter__game=game
        )
        context["visitor_points"] = Point.objects.filter(
            player__team=game.team_visitor,
            quarter__game=game
        )

        context["local_fouls"] = Foul.objects.filter(
            player__team=game.team_local,
            quarter__game=game
        )
        context["visitor_fouls"] = Foul.objects.filter(
            player__team=game.team_visitor,
            quarter__game=game
        )

        init_context(context, game.day.tournament, get_team(self.request.user))

        return context


class BracketView(generic.TemplateView):
    template_name = "tournaments/bracket.html"


class StatisticsView(generic.TemplateView):
    template_name = "tournaments/stats.html"

    class StandingsEntry:
        def __init__(self, team_name, wins, points):
            self.team_name = team_name
            self.wins = wins
            self.points = points

    def get_context_data(self, **kwargs):
        try:
            tournament = Tournament.objects.get(id=self.kwargs['tournament'])
        except Tournament.DoesNotExist:
            raise Http404()

        context = super().get_context_data(**kwargs)

        init_context(context, tournament, get_team(self.request.user))

        context["filter"] = Region.objects.all()

        _filter = self.request.GET.get("filter")
        if _filter is None:
            _filter = "general"

        context["current_filter"] = _filter

        standings = []

        if _filter == "general":
            team_wins = tournament.team_set.annotate(wins=Count("win")).order_by("-wins")
            points = tournament.team_set.annotate(points=Coalesce(Sum("player__point__value"), 0))
        else:
            team_wins = tournament.team_set.filter(state__region__name=_filter).annotate(wins=Count("win")).order_by("-wins")
            points = tournament.team_set.filter(state__region__name=_filter).annotate(points=Coalesce(Sum("player__point__value"), 0))

        for entry in team_wins:
            standings.append(self.StandingsEntry(entry.name, entry.wins, points.get(id=entry.id).points))

        context["standings"] = standings

        context["filtered_teams"] = Region.objects.annotate(teams=Count("state_set__team")).values("name", "teams")

        context["is_region_filter"] = True

        return context


class TournamentDetailView(generic.DetailView):
    template_name = 'tournaments/tournamentDetail.html'
    model = Tournament


class TeamDetailView(generic.DetailView):
    template_name = "tournaments/team.html"
    model = Team
    context_object_name = "t"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        init_context(context, Tournament.objects.get(id=self.kwargs["tournament"]), get_team(self.request.user))
        team = Team.objects.get(id=self.kwargs["pk"])
        context["player_list"] = Player.objects.filter(team=team)
        if team.code is None:
            team.generate_code()
        try:
            Coach.objects.get(user=self.request.user)
            context["is_coach"] = True
        except Coach.DoesNotExist:
            context["is_coach"] = False
            context["player_viewable_id"] = Player.objects.get(user=self.request.user).id
        return context

    def dispatch(self, request, *args, **kwargs):
        url = "/tournaments/"
        if self.request.user.is_active and not self.request.user.is_superuser:
            try:
                p = Player.objects.get(user=self.request.user)
                if p.team != Team.objects.get(id=self.kwargs["pk"]):
                    return redirect(url)
            except Player.DoesNotExist:
                if str(Coach.objects.get(user=self.request.user).team.id) != self.kwargs["pk"]:
                    return redirect(url)
        else:
            return redirect(url)
        return super(TeamDetailView, self).dispatch(request, *args, **kwargs)


class StatisticsViewState(generic.TemplateView):
    template_name = "tournaments/stats.html"

    class StandingsEntry:
        def __init__(self, team_name, wins, points):
            self.team_name = team_name
            self.wins = wins
            self.points = points

    def get_context_data(self, **kwargs):
        try:
            tournament = Tournament.objects.get(id=self.kwargs['tournament'])
        except Tournament.DoesNotExist:
            raise Http404()

        context = super().get_context_data(**kwargs)

        init_context(context, tournament, get_team(self.request.user))

        context["filter"] = State.objects.all()

        _filter = self.request.GET.get("filter")
        if _filter is None:
            _filter = "general"

        context["current_filter"] = _filter

        standings = []

        if _filter == "general":
            team_wins = tournament.team_set.annotate(wins=Count("win")).order_by("-wins")
            points = tournament.team_set.annotate(points=Coalesce(Sum("player__point__value"), 0))
        else:
            team_wins = tournament.team_set.filter(state__name=_filter).annotate(wins=Count("win")).order_by("-wins")
            points = tournament.team_set.filter(state__name=_filter).annotate(
                points=Coalesce(Sum("player__point__value"), 0))

        for entry in team_wins:
            standings.append(self.StandingsEntry(entry.name, entry.wins, points.get(id=entry.id).points))

        context["standings"] = standings

        context["filtered_teams"] = State.objects.annotate(teams=Count("team"))

        return context


class PlayerView(generic.DetailView):
    template_name = "users/player.html"
    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        init_context(context, Tournament.objects.get(id=self.kwargs["tournament"]), get_team(self.request.user))
        return context

    def dispatch(self, request, *args, **kwargs):
        url = "/tournaments/"
        if self.request.user.is_active:
            try:
                p = Player.objects.get(user=self.request.user)
                if str(p.id) != self.kwargs["pk"]:
                    return redirect(url)
            except Player.DoesNotExist:
                if Coach.objects.get(user=self.request.user).team != Player.objects.get(id=self.kwargs["pk"]).team:
                    return redirect(url)
        else:
            return redirect(url)
        return super(PlayerView, self).dispatch(request, *args, **kwargs)


def regenerate_code(request, *args, **kwargs):
    Team.objects.get(id=kwargs["pk"]).generate_code()
    return redirect("/tournaments/" + kwargs["tournament"] + "/teams/" + kwargs["pk"] + "/")


class GamesViewAPI(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
