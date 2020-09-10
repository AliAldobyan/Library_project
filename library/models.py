from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    year_of_release = models.DateField()
    isbn = models.IntegerField()
    genre = models.CharField(max_length=120)
    available= models.BooleanField()
    borrowed = models.BooleanField()


    def __str__(self):
    	return self.name
