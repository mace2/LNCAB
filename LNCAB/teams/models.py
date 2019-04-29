from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Sex(models.Model):
    name = models.CharField("name",max_length=20, choices=(
                               ('M', 'Masculine'),
                               ('F', 'Feminine')

                           ))

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField("name",max_length=100,choices=(('U-13','U-13'),
                            ('U-15','U-15'),
                            ('U-17','U-17'),
                            ('U-19', 'U-19')
                            )
                            )

    def __str__(self):
        return str(self.name)


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
    code = models.TextField(null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex,on_delete=models.CASCADE)

    def __str__(self):
        return self.name +" from "+str(self.state)+" "+ str(self.category)+' - '+str(self.sex)

    def generate_code(self):
        self.save()
        self.code = User.objects.make_random_password(length=4, allowed_chars='0123456789') + str(self.id)
        self.save()


