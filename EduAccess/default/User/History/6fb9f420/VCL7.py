from django.db import models
from school.models import Staff
# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length=100)
    librarian = models.ForeignKey(Staff, on_delete=models.CASCADE)
    on_duty = models.BooleanField(default=False)
    def __str__(self):
        return f'Name -- {self.name}, librarian on duty {self.librarian}'


class Books(models.Model):
    title = models.CharField(max_length=200)
    quantity = models.SmallIntegerField()
    last_accessed =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name -- {self.title}, count-- {self.quantity}, last_accessed -- {self.last_accessed}'