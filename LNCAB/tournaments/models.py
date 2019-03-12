from django.db import models

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField("start_date")
    teams = models.ManyToManyField('teams.Team')

    def __str__(self):
        return self.name

class Jornada(models.Model):
    opciones_jornada=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('1000','1000'),
    )
    jornada=models.CharField(max_length=4,choices=opciones_jornada)
    torneo=models.ForeignKey(Tournament,on_delete=models.CASCADE)

    opciones=(
        ('IZ','InterZona'),
        ('Z','Zona'),
    )
    start_date=models.DateTimeField("Start Date")
    end_date = models.DateTimeField("End Date")
    tipo=models.CharField(max_length=2,choices=opciones)


    def __str__(self):

        return self.torneo.name+" Jornada "+str(self.jornada)+" ("+self.tipo +")"



class Game(models.Model):
    date = models.DateTimeField("date")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    teamLocal=models.ForeignKey('teams.Team', on_delete=models.CASCADE,related_name='LocalTeam')
    teamVisitante = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='VisitanteTeam')
    jornada=models.ForeignKey(Jornada,on_delete=models.CASCADE)

    def __str__(self):
        return "Juego "+str(self.pk)+ " de "+str(self.jornada)






