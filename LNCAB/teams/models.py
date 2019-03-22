from django.db import models
import random
from users.models import Coach
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


class Zone(models.Model):
    name = models.CharField("name", max_length=50)
    code = models.CharField("code", max_length=5)
    region_set = models.ManyToManyField(State)

    def __str__(self):
        return self.name


class Team(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    address = models.CharField("address", max_length=200)
    name = models.CharField("name", max_length=50)
    code = models.IntegerField(default=random.randint(1000, 9999))

    def __str__(self):
        return self.name

