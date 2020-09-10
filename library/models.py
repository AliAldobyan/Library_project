from django.db import models
from django.contrib.auth.models import User


# Genre model


class Book(models.Model):
    name = models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    year_of_release = models.DateField()
    isbn = models.IntegerField()
    genre = models.CharField(max_length=120)
    # genres = models.ManyToManyField(Genre)
    available= models.BooleanField()
    borrowed = models.BooleanField()

    def __str__(self):
    	return self.name
