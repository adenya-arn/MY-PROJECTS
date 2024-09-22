from django.db import models
from school.models import Staff
# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(Staff, on_delete=models.PROTECT) 
