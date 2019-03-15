from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Game, Tournament


class GamesView(generic.ListView):
    template_name = 'tournaments/index.html'

    def get_queryset(self):
        return Game.objects.all()

