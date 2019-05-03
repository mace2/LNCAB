"""LNCAB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tournaments.views import GamesView, DetailView, BracketView, TeamDetailView, StatisticsView, StatisticsViewState,TournamentsView, TournamentDetailView,TeamsView,myGamesView


urlpatterns = [
    path('users/', include('users.urls')),
    path('teams/', include('teams.urls')),
    path('admin/', admin.site.urls),
   # path('teams/', include('teams.urls')),
    path('tournaments/', TournamentsView.as_view()),

    path('tournaments/<pk>/mygames', myGamesView.as_view()),
    path('tournaments/<pk>/day/<day>/', GamesView.as_view()),
    path('tournaments/<tournament>/games/<pk>/', DetailView.as_view()),
    path('tournaments/<tournament>/stats/', StatisticsView.as_view()),
    path('tournaments/<tournament>/playoffs/', StatisticsViewState.as_view()),
    path('tournaments/<pk>/teams/',TeamsView.as_view()),
    path('tournaments/<tournament>/teams/<pk>/', TeamDetailView.as_view()),
    path('tournaments/bracket/', BracketView.as_view()),
    path('tournaments/<pk>/', TournamentDetailView.as_view()),

]
urlpatterns+=staticfiles_urlpatterns()
