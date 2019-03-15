from django.db import models


# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField("start_date")
    teams = models.ManyToManyField('teams.Team')

    def __str__(self):
        return self.name


class Day(models.Model):
    number=models.IntegerField()
    isInterZone=models.BooleanField()
    start_dateTime = models.DateTimeField("Start DateTime")
    end_dateTime = models.DateTimeField("End DateTime", null=True, blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.tournament.name+" Day "+str(self.number) + \
               " (" + "InterZone" if self.isInterZone else "Zone" + ")"


class Venue(models.Model):
    name=models.CharField("name", max_length=200)
    courts=models.PositiveIntegerField("Courts", default=6)
    address = models.CharField(max_length=200)
    state = models.ForeignKey('teams.State', on_delete=models.CASCADE)

    def __str__(self):
        return self.name+" ,  "+ str(self.state)


class Game(models.Model):
    dateTime = models.DateTimeField("dateTime")
    tournament = models.ForeignKey(Tournament,  on_delete=models.CASCADE)
    teamLocal = models.ForeignKey('teams.Team',  on_delete=models.CASCADE, related_name='LocalTeam')
    teamVisitor = models.ForeignKey('teams.Team',  on_delete=models.CASCADE,  related_name='VisitanteTeam')
    number = models.IntegerField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    court = models.IntegerField()

    def __str__(self):
        return "Juego "+str(self.number)+ " de "+str(self.day)+" "+self.teamLocal.name+" vs "+self.teamVisitor.name







