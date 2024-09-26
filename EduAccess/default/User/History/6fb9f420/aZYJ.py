from django.db import models
from school.models import Staff, Class, Subject
# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=100)
    librarian = models.ForeignKey(Staff, on_delete=models.PROTECT)
    on_duty = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
    
class Librarian(models.Model):
    information = models.ForeignKey(Staff, on_delete=models.PROTECT)




class Book(models.Model):
    title = models.CharField(max_length=200)
    quantity = models.SmallIntegerField()
    last_accessed = models.DateTimeField(auto_now=True)
    classes = models.ForeignKey(Class, on_delete=models.PROTECT)
    subjects = models.ForeignKey(Subject    , on_delete=models.PROTECT)

    def __str__(self):
        return f'Name -- {self.title}, count-- {self.quantity}, last_accessed -- {self.last_accessed}'


class Request (models.Model):
    who = models.CharField(max_length=100, null=True, blank=True)
    when = models.DateTimeField(auto_now=True)

