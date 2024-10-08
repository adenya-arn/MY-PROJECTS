from django.db import models
from school.models import Staff 
# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(Staff, on_delete=models.PROTECT) 
    on_duty = models.BooleanField(default=False)

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.SmallIntegerField()
    last_accessed = models.DateTimeField(auto_now=True)
    store = models.ManyToManyField(Store)

""" Model which keeps Records
class Requests (models.Model):
    who = models.OneToOneField()"""

