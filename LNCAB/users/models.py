from django.db import models

# Create your models here.


class Coach(models.Model):
    name = models.CharField("name", max_length=200)
    last_names = models.CharField(max_length=200)
    telephone = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField("start_date")
    end_date = models.DateField("end_date", null=True, blank=True)

    def __str__(self):
        return self.name+" "+self.last_names


class Team(models.Model):
    name= models.CharField("Nombre de Equipo",max_length=50)
    nombre_Coach = models.OneToOneField(Coach, related_name="tournamentp", on_delete=models.CASCADE)
    city=models.CharField("Ciudad",default="Temp",max_length=50)
    cede = models.CharField("Cede",max_length=200)

    def __str__(self):
        return self.name


class Scorekeeper(models.Model):
    name = models.CharField("name", max_length=200)
    last_names = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField("name", max_length=200)
    last_names = models.CharField(max_length=200)
    dob = models.DateField("Date Of Birth")
    telephone = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100, null=True, blank=True)
    points = models.PositiveSmallIntegerField("Points",null=True, blank=True)
    fouls = models.PositiveSmallIntegerField("Fouls", null=True, blank=True)

    def __str__(self):
        return self.name+" "+self.last_names
