from django.db import models
from school.models import Staff
# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=100)
    librarian = models.ForeignKey(Staff, on_delete=models.CASCADE)


class Books(models.Model):
    pass


