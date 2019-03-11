from django.db import models
# Create your models here.


class State(models.Model):
    name = models.CharField("name", max_length=50)
    code = models.CharField("code", max_length=5)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField("name", max_length=50)
    code = models.CharField("code", max_length=5)
    state_set = models.ManyToManyField(State)

    def __str__(self):
        return self.name


class Team(models.Model):
    coach = models.OneToOneField('users.Coach', on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    address = models.CharField("address", max_length=200)
    name = models.CharField("name", max_length=50)

    def __str__(self):
        return self.name

