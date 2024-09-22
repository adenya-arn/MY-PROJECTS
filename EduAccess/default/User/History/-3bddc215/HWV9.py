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
    parent = models.OneToOneField('Parents', on_delete=models.SET_NULL, related_name='child')
    results = models.ForeignKey('Grades', on_delete=models.CASCADE, related_name='grades')
    subjects = models.ForeignKey('Subjects', on_delete=models.SET_NULL, related_name='subjects')

class Classes (models.Model):
    number = models.SmallIntegerField()
    stream = models.CharField(max_length=50)

class Grades (models.Model):
    marks = models.SmallIntegerField()
    grade = models.CharField(max_length=10)

class Subjects (models.Model):
    name = models.CharField(max_length=200)

class Parents (models.Model):
    id_no = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    child = models.ManyToManyField(Students)

class Roles (models.Model):
    name = models.CharField(max_length=100)