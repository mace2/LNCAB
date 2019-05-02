from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

from django.views import generic
from tournaments.models import Game, Tournament, Day, Point, Foul, Win
from users.models import Player
from teams.models import Team, Region
from django.template import loader
from django.db.models import Count, Sum


