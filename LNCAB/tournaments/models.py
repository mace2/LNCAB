from django.db import models

# Create your models here.


class Game(models.Model):
<<<<<<< HEAD
    name_team1 = models.ForeignKey('teams.Team', on_delete=models.CASCADE)
=======
    date = models.DateTimeField("date")
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    teamLocal=models.ForeignKey('teams.Team', on_delete=models.CASCADE,related_name='LocalTeam')
    teamVisitante = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='VisitanteTeam')

    def __str__(self):
        return self.name

>>>>>>> AndresQuiroz

    def __str__(self):
        return self.name_team1
