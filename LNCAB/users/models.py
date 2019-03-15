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
<<<<<<< .merge_file_a02916
=======

class Team(models.Model):
    name= models.CharField("Nombre de Equipo",max_length=50)
    nombre_Coach = models.OneToOneField(Coach, on_delete=models.CASCADE)
    city=models.CharField("Ciudad",default="Temp",max_length=50)
    cede = models.CharField("Cede",max_length=200)


    def __str__(self):
        return self.name

class Scorekeeper (models.Model):
<<<<<<< .merge_file_a06516
<<<<<<< .merge_file_a01120
<<<<<<< .merge_file_a12744
<<<<<<< .merge_file_a10704
  nombre_Scorekeeper = models.CharField("Nombre del Anotador",max_length=50)
>>>>>>> .merge_file_a02984
=======
  nombre_Scorekeeper = models.CharField("Nombre del Anotador",max_length=50)
>>>>>>> .merge_file_a05588
=======
  nombre_Scorekeeper = models.CharField("Nombre del Anotador",max_length=50)
>>>>>>> .merge_file_a09144
=======
  nombre_Scorekeeper = models.CharField("Nombre del Anotador",max_length=50)
>>>>>>> .merge_file_a13468
=======
  nombre_Scorekeeper = models.CharField("Nombre del Anotador",max_length=50)
>>>>>>> .merge_file_a14184
