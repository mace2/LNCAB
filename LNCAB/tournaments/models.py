from django.db import models

# Create your models here.


class Game(models.Model):
    name_team1 = models.ForeignKey('teams.Team', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_team1
