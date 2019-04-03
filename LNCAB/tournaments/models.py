from django.db import models
from users.models import Scorekeeper, Player
from teams.models import Team
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum


# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField("start_date")
    end_date = models.DateField("start_date", null=True, blank=True)
    team_set = models.ManyToManyField('teams.Team')

    def __str__(self):
        return self.name + " (" + str(self.start_date) + ((" - " + str(self.end_date)) if self.end_date else "") + ")"


class Day(models.Model):
    number = models.IntegerField()
    is_inter_zone = models.BooleanField()
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date", null=True, blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.tournament.name+" Day " + str(self.number) + \
               ", " + str(self.start_date) + " (" + ("inter-zone" if self.is_inter_zone else "not inter-zone") + ")"


class Venue(models.Model):
    name = models.CharField("name", max_length=200)
    courts = models.PositiveIntegerField("Courts", default=6)
    address = models.CharField(max_length=200)
    state = models.ForeignKey('teams.State', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ", " + str(self.state)


class Point(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    value = models.IntegerField(validators=[
        MaxValueValidator(3),
        MinValueValidator(1)
    ])

    def __str__(self):
        return ""


class Foul(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    type = models.CharField(
        choices=(
            ('1', '1'),
            ('2', '2'),
            ('3', '3')
        ),
        max_length=20
    )

    def __str__(self):
        return ""


class Game(models.Model):
    date_time = models.DateTimeField("dateTime")
    team_local = models.ForeignKey('teams.Team',  on_delete=models.CASCADE, related_name='LocalTeam')
    team_visitor = models.ForeignKey('teams.Team',  on_delete=models.CASCADE,  related_name='VisitanteTeam')
    number = models.IntegerField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    court = models.IntegerField()
    scorekeeper = models.ForeignKey(Scorekeeper, on_delete=models.CASCADE, null=True, blank=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return "Game " + str(self.number) + " day " + str(self.day.number) + " of " + self.day.tournament.name \
               + ": " + self.team_local.name + " vs " + self.team_visitor.name \
               + (" (finished)" if self.is_finished else " (not played yet)")

    def get_local_points(self):
        return Point.objects.filter(game=self, player__team=self.team_local).aggregate(Sum('value'))['value__sum']

    def get_visitor_points(self):
        return Point.objects.filter(game=self, player__team=self.team_visitor).aggregate(Sum('value'))['value__sum']

    def get_local_fouls(self):
        return Foul.objects.filter(game=self, player__team=self.team_local).count()

    def get_visitor_fouls(self):
        return Foul.objects.filter(game=self, player__team=self.team_visitor).count()


class Win(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.team.name + " won a match in " + self.tournament.name
