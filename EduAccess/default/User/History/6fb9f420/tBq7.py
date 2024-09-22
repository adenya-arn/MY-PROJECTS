from django.db import models

# Create your models here.


class Library(models.Model):
    name =models.CharField(max_length=100)


class Books(models.Model):
    pass


