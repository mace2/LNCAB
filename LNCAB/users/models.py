from django.db import models

# Create your models here.


class Coach(models.Model):
    name = models.CharField(max_length=200)
    last_names = models.CharField(max_length=200)
    telephone = git models.CharField(max_length=100)
    start_date = models.DateTimeField("start date")
    end_date = models.DateTimeField("start date")
