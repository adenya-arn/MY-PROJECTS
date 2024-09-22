from django.db import models
from school.models import Staff, Classes, Subjects
# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=100)
    librarian = models.ForeignKey(Staff, on_delete=models.PROTECT)
    on_duty = models.BooleanField(default=False)
    def __str__(self):
        return f'Name -- {self.name}, librarian on duty {self.librarian}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    quantity = models.SmallIntegerField()
    last_accessed = models.DateTimeField(auto_now=True)
    classes = models.ForeignKey(Classes, on_delete=models.PROTECT)
    subjects = models.ForeignKey(Subjects, on_delete=models.PROTECT)

    def __str__(self):
        return f'Name -- {self.title}, count-- {self.quantity}, last_accessed -- {self.last_accessed}'
    
""" Model which keeps Records
class Requests (models.Model):
    who = models.OneToOneField()"""

