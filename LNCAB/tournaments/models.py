from django.db import models

# Create your models here.


class Game(models.Model):
    date = models.DateTimeField("date")


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField("start_date")
    teams = models.ManyToManyField('teams.Team')
    games = models.ManyToManyField(Game)

    def __str__(self):
        return self.name


