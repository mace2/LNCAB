from django.db import models

import random

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
    category = models.CharField(max_length=100,
    choices=(
        ('U-15','U-15'),
        ('U-16', 'U-16'),
        ('U-17', 'U-17')
        )
    )

    sex = models.CharField(max_length=100,
                           choices=(
                               ('M', 'Masculino'),
                               ('F', 'Femenino')

                           ))


    def __str__(self):
        return self.name + self.category+'-'+self.sex

