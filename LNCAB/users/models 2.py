from django.db import models

# Create your models here.


class Coach(models.Model):
    name = models.CharField("name", max_length=200)
    last_names = models.CharField(max_length=200)
    telephone = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100, null=True)
    start_date = models.DateField("start_date")
    end_date = models.DateField("end_date", null=True)

    def __str__(self):
        return self.name+" "+self.last_names