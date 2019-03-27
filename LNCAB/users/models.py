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
    name = models.CharField("Name", max_length=200)
    last_names = models.CharField("Last names", max_length=200)
    date_of_birth = models.DateField("Birth date")
    telephone = models.CharField("Telephone", max_length=100)
    email_address = models.CharField("Email", max_length=100, null=True, blank=True)
    code = models.CharField("Team code",max_length=200)
    sex = models.CharField(max_length=100,
                           choices=(
                               ('M', 'Masculine'),
                               ('F', 'Feminine')

                           ))

    def __str__(self):
        return self.name+" "+self.last_names
