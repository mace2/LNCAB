from django.db import models

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField("start_date")
    teams = models.ManyToManyField('teams.Team')

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateTimeField("date")
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)


