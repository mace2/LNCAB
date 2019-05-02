from django.db import models
from users.models import Scorekeeper, Player
from teams.models import Team,Sex,Category

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum, Count, Q
from django.db.models.functions import Coalesce
from django.core.exceptions import ObjectDoesNotExist



# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField("start_date")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex,on_delete=models.CASCADE)
    end_date = models.DateField("start_date", null=True, blank=True)
    team_set = models.ManyToManyField('teams.Team')
    is_active = models.BooleanField()

    def get_current_day(self):
        try:
            day = Day.objects.filter(tournament=self)\
                .annotate(unfinished=Count("game", filter=Q(game__is_finished=False))) \
                .filter(unfinished__gt=0)\
                .order_by("start_date").first()
        except Day.DoesNotExist:
            day = Day.objects.filter(tournament=self).order_by("-start_date").first()
        if day is None:
            day = Day.objects.filter(tournament=self).order_by("-start_date").first()
        return day

    def __str__(self):
        return self.name+" " + "Category: "+str(self.category )+ " "+str(self.sex)


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


class Quarter(models.Model):
    number = models.IntegerField(validators=[
        MaxValueValidator(4),
        MinValueValidator(1)
    ])
    game = models.ForeignKey('Game', on_delete=models.CASCADE)


class Point(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE)
    value = models.IntegerField(validators=[
        MaxValueValidator(3),
        MinValueValidator(1)
    ])

    def __str__(self):
        return ""


class Foul(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE)
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

    def get_all_points(self, team):
        return Point.objects.filter(quarter__game=self, player__team=team).aggregate(value__sum=Coalesce(Sum('value'), 0))['value__sum']

    def get_points_by_quarter(self, team, num):
        return Point.objects.filter(quarter__game=self, player__team=team, quarter__number=num).aggregate(value__sum=Coalesce(Sum('value'), 0))['value__sum']

    def get_all_fouls(self, team):
        return Foul.objects.filter(quarter__game=self, player__team=team).count()

    def get_fouls_by_quarter(self, team, num):
        return Foul.objects.filter(quarter__game=self, player__team=team, quarter__number=num).count()

    def local_points(self):
        return self.get_all_points(self.team_local)

    def visitor_points(self):
        return self.get_all_points(self.team_visitor)

    def local_fouls(self):
        return self.get_all_fouls(self.team_local)

    def visitor_fouls(self):
        return self.get_all_fouls(self.team_visitor)

    def local_q1(self):
        return self.get_points_by_quarter(self.team_local, 1)

    def local_q2(self):
        return self.get_points_by_quarter(self.team_local, 2)

    def local_q3(self):
        return self.get_points_by_quarter(self.team_local, 3)

    def local_q4(self):
        return self.get_points_by_quarter(self.team_local, 4)

    def visitor_q1(self):
        return self.get_points_by_quarter(self.team_visitor, 1)

    def visitor_q2(self):
        return self.get_points_by_quarter(self.team_visitor, 2)

    def visitor_q3(self):
        return self.get_points_by_quarter(self.team_visitor, 3)

    def visitor_q4(self):
        return self.get_points_by_quarter(self.team_visitor, 4)

    def finish(self):
        if self.get_all_points(self.team_local) > self.get_all_points(self.team_visitor):
            Win.objects.create(team=self.team_local, tournament=self.day.tournament)
        else:
            Win.objects.create(team=self.team_visitor, tournament=self.day.tournament)
        self.is_finished = True
        self.save()


class Win(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.team.name + " won a match in " + self.tournament.name


