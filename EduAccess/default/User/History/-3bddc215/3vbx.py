from django.db import models

# Create your models here.


class Staff (models.Model):
    id_no = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    position = models.OneToOneField('Position', on_delete=models.PROTECT)    

class Students (models.Model):
    reg_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    stream = models.ForeignKey('Classes', on_delete=models.PROTECT, related_name='classes')
    parent = models.ManyToManyField('Parents', on_delete=models.SET_NULL, related_name='child')

class Classes (models.Model):
    pass

class Grades (models.Model):
    pass

class Subjects (models.Model):
    pass

class Parents (models.Model):
    id_no = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)

class Position (models.Model):
    name = models.CharField(max_length=100)