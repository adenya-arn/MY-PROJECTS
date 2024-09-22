from django.db import models

# Create your models here.

class Roles (models.Model):
    name = models.CharField(max_length=100)

class Staff (models.Model):
    id_no = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    position = models.OneToOneField(Roles, on_delete=models.PROTECT)    


class Classes (models.Model):
    number = models.SmallIntegerField()
    stream = models.CharField(max_length=50)
    ###performance = models. (should add functionality for one to see class performance)

class Grades (models.Model):
    marks = models.SmallIntegerField()
    grade = models.CharField(max_length=10)
    student = models.ForeignKey('Students', on_delete=models.PROTECT) 


class Subjects (models.Model):
    name = models.CharField(max_length=200)


class Parents (models.Model):
    id_no = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    child = models.ManyToManyField('Students')


class Students (models.Model):
    reg_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    stream = models.ForeignKey(Classes, on_delete=models.PROTECT, related_name='classes')
    parent = models.OneToOneField(Parents, on_delete=models.SET_NULL, related_name='child')
    results = models.ForeignKey(Grades, on_delete=models.CASCADE, related_name='grades')
    subjects = models.ForeignKey(Subjects, on_delete=models.SET_NULL, related_name='subjects')