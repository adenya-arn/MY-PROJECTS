from django.db import models
from school.models import Staff
# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=100)
    librarian = models.ForeignKey(Staff, on_delete=models.CASCADE)


class Books(models.Model):
    title = models.CharField(max_length=200)
    quantity = models.SmallIntegerField()
    last_accessed =models.DateTimeField(auto_now_add=True)


