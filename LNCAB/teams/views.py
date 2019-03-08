from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Team


def index(request):
    template = loader.get_template('teams/base.html')
    teams = Team.objects.all()
    context={"teams":teams,
    }

    return HttpResponse(template.render(context,request))