from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

from django.views import generic
from .models import Game, Tournament, Day


class GamesView(generic.ListView):
    template_name = 'tournaments/index.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        try:
            self.day = Day.objects.get(number=self.kwargs['day'])
        except Day.DoesNotExist:
            raise Http404()
        return self.day.game_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prev_day"] = self.day.number - 1
        context["next_day"] = self.day.number + 1
        return context


