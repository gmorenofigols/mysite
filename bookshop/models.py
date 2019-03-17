from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    year_born = models.DateField()
    description = models.TextField()

    def __str__(self):
        return "%s - %s" % (self.name, self.year_born)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    release_date = models.DateField()
    genre = models.CharField(max_length=20)
    editorial = models.CharField(max_length=20)
    cost = models.IntegerField()
    resume = models.TextField()

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.author, self.genre)
