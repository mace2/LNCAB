from django.db import models
from teams.models import Team, State
from django.contrib.auth.models import User

# Create your models here.


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=100)
    start_date = models.DateField("start_date")
    end_date = models.DateField("end_date", null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name


class Scorekeeper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # code = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField("Birth date")
    telephone = models.CharField("Telephone", max_length=100)
    sex = models.CharField(max_length=100,
                           choices=(
                               ('M', 'Masculine'),
                               ('F', 'Feminine')

                           ))

    def __str__(self):
        return str(self.user)
