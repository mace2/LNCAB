from django.db import models

# Create your models here.


class Coach(models.Model):
    name = models.CharField("Nombre Coach",max_length=200)
    last_names = models.CharField(max_length=200)
    telephone = models.CharField(max_length=100)
    start_date = models.DateTimeField("start date")
    end_date = models.DateTimeField("end date")

    def __str__(self):
        return self.name+" "+self.last_names

class Team(models.Model):
    name= models.CharField("Nombre de Equipo",max_length=50)
    nombre_Coach = models.OneToOneField(Coach, on_delete=models.CASCADE)
    city=models.CharField("Ciudad",default="Temp",max_length=50)
    cede = models.CharField("Cede",max_length=200)




    def __str__(self):
        return self.name

