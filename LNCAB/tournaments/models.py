from django.db import models

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField("start_date")
    teams = models.ManyToManyField('teams.Team')

    def __str__(self):
        return self.name

class Jornada(models.Model):
    torneo=models.ForeignKey(Tournament,on_delete=models.CASCADE)
    opciones=(
        ('IZ','InterZona'),
        ('Z','Zona'),
    )
    start_date=models.DateTimeField("Start Date")
    end_date = models.DateTimeField("End Date")
    tipo=models.CharField(max_length=2,choices=opciones)


    def __str__(self):

        return self.torneo.name+" Jornada "+str(self.pk)+" ("+self.tipo +")"



class Game(models.Model):
    date = models.DateTimeField("date")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    teamLocal=models.ForeignKey('teams.Team', on_delete=models.CASCADE,related_name='LocalTeam')
    teamVisitante = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='VisitanteTeam')
    jornada=models.ForeignKey(Jornada,on_delete=models.CASCADE)

    def __str__(self):
        return "Juego "+str(self.pk)+ " de "+str(self.jornada)






