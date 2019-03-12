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



class Cede(models.Model):
    name=models.CharField("Nombre",max_length=200)
    canchas=models.PositiveIntegerField("Numero de Canchas",default=6)
    direccion = models.CharField(max_length=200)
    ciudad = models.ForeignKey('teams.State',on_delete=models.CASCADE)

    def __str__(self):
        return self.name+" , "+ str(self.ciudad)


class Game(models.Model):
    date = models.DateTimeField("date")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    teamLocal=models.ForeignKey('teams.Team', on_delete=models.CASCADE,related_name='LocalTeam')
    teamVisitante = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='VisitanteTeam')
    juego_opciones = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
    )
    juego=models.CharField(max_length=2,choices=juego_opciones)
    jornada=models.ForeignKey(Jornada,on_delete=models.CASCADE)
    cede=models.ForeignKey(Cede,on_delete=models.CASCADE)



    def __str__(self):
        return "Juego "+str(self.juego)+ " de "+str(self.jornada)+" "+self.teamLocal.name+" vs "+self.teamVisitante.name







