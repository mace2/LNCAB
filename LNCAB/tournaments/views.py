from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.db.models import Q

from django.views import generic
from .models import Game, Tournament, Day, Point, Foul, Win
from django.contrib.auth.models import User
from users.models import Player
from teams.models import Team, Region
from django.template import loader

from django.db.models import Count, Sum


def init_context(context, tournament):
    context["day"] = tournament.get_current_day().number
    context["tournament"] = tournament.pk


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
        init_context(context, tournament)
        return context




class myGamesView(generic.ListView):
    template_name = "tournaments/my_games.html"
    context_object_name = "my_games_list"



    def get_queryset(self):
        player_pk = self.request.user.pk
        team_id = Player.objects.get(id=player_pk).team.id
        games = Game.objects.filter(Q(team_local=team_id) | Q(team_visitor=team_id))
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

        init_context(context, self.day.tournament)

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

        init_context(context, game.day.tournament)

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

        init_context(context, tournament)

        context["regions"] = Region.objects.all()
        curr = 0
        # last = -1

        standings = []
        point_leaders = []
        foul_leaders = []

        region = self.request.GET.get("region")
        if region is None:
            region = "general"
        context["region"] = region
        if region == "general":
            wins = Win.objects.filter(tournament=tournament) \
                       .values('team__name').annotate(wins=Count('team')).order_by('-wins')[:10]

            no_wins = tournament.team_set.exclude(id__in=Win.objects.filter(tournament=tournament).values("team__id")) \
                .all().values("name")

            points = Point.objects.filter(quarter__game__day__tournament=tournament) \
                         .values('player__team__name').annotate(points=Sum('value')).order_by('-points')[:10]

            no_points = tournament.team_set.exclude(
                id__in=Point.objects.filter(quarter__game__day__tournament=tournament).values("player__team__id")
            )

            fouls = Foul.objects.filter(quarter__game__day__tournament=tournament) \
                        .values('player__team__name').annotate(fouls=Count('quarter__game')).order_by('-fouls')[:10]

            no_fouls = context["teams_no_fouls"] = tournament.team_set.exclude(
                id__in=Foul.objects.filter(quarter__game__day__tournament=tournament).values("player__team__id")
            )
        else:
            wins = Win.objects.filter(tournament=tournament, team__state__region__name=region) \
                       .values('team__name').annotate(wins=Count('team')).order_by('-wins')[:10]

            no_wins = tournament.team_set.exclude(id__in=Win.objects.filter(tournament=tournament).values("team__id")) \
                .filter(state__region__name=region).values("name")

            points = Point.objects.filter(quarter__game__day__tournament=tournament,
                                          player__team__state__region__name=region) \
                         .values('player__team__name').annotate(points=Sum('value')).order_by('-points')[:10]

            no_points = tournament.team_set.exclude(
                id__in=Point.objects.filter(quarter__game__day__tournament=tournament).values("player__team__id")
            ).filter(state__region__name=region)

            fouls = Foul.objects.filter(quarter__game__day__tournament=tournament,
                                        player__team__state__region__name=region) \
                        .values('player__team__name').annotate(fouls=Count('quarter__game')).order_by('-fouls')[:10]

            no_fouls = context["teams_no_fouls"] = tournament.team_set.exclude(
                id__in=Foul.objects.filter(quarter__game__day__tournament=tournament).values("player__team__id")
            ).filter(state__region__name=region)

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
            standings.append(self.StandingsEntry(place=curr, team=entry["name"], value=0))

        context["standings"] = standings
        # points
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
            point_leaders.append(self.StandingsEntry(place=curr, team=entry.name, value=0))

        context["point_leaders"] = point_leaders

        # fouls
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
            foul_leaders.append(self.StandingsEntry(place=curr, team=entry.name, value=0))

        context["foul_leaders"] = foul_leaders

        context["teams_by_state"] = tournament\
            .team_set.values('state__name')\
            .annotate(number=Count('id'))\
            .order_by('-number')

        return context


class TournamentDetailView(generic.DetailView):
    template_name = 'tournaments/tournamentDetail.html'
    model = Tournament
