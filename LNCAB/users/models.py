from django.db import models
from teams.models import Team, State

# Create your models here.


class Coach(models.Model):
    name = models.CharField("name", max_length=200)
    last_names = models.CharField(max_length=200)
    telephone = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField("start_date")
    end_date = models.DateField("end_date", null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name+" "+self.last_names


class Scorekeeper(models.Model):
    name = models.CharField("name", max_length=200)
    last_names = models.CharField(max_length=200)
    telephone = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField("Nombre", max_length=200)
    last_names = models.CharField("Apellidos",max_length=200)
    date_of_birth = models.DateField("Dia de nacimiento")
    telephone = models.CharField("Telefono",max_length=100)
    email_address = models.CharField("Direecion de correo",max_length=100, null=True, blank=True)
    code = models.CharField("Codigo de Equipo",max_length=200)


    def __str__(self):
        return self.name+" "+self.last_names
