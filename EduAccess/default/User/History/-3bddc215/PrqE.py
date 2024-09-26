from django.db import models

# Create your models here.

class Role (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Staff (models.Model):
    id_no = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    position = models.OneToOneField(Role, on_delete=models.PROTECT)  

    def ___str__(self):
        return f'ID -- {self.id_no} -- name {self.name} -- {self.position}'  


class Stream (models.Model):
    letter = models.CharField(max_length=10)

    def __str__(self):
        return self.letter


class Class (models.Model):
    number = models.SmallIntegerField()
    stream = models.OneToOneField(Stream, on_delete=models.PROTECT, unique=True)

    def __str__(self):
        return f'{self.number} {self.stream}'

class Grade (models.Model):
    marks = models.SmallIntegerField()
    grade = models.CharField(max_length=10)
    student = models.ForeignKey('Student', on_delete=models.PROTECT, related_name='student') 

    def __str__ (self):
        return f'{self.student} {self.grade}'


class Subject (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Parent (models.Model):
    id_no = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    child = models.ManyToManyField('Student', related_name='parents')

    def __str__(self):
        return self.name


class Student (models.Model):
    reg_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    stream = models.ForeignKey(Class, on_delete=models.PROTECT, related_name='classes')
    parent = models.OneToOneField(Parent, on_delete=models.PROTECT, related_name='children')
    results = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='grades')
    subjects = models.ForeignKey(Subject, on_delete=models.SET_NULL, related_name='subjects', null=True)

    def __str__(self):
        return f'{self.name} -- {self.reg_no}'
    

class Performance (models.Model):
    stream = models.CharField(max_length=100, blank=True, null=True)
    average = models.SmallIntegerField()


    def __str__ (self):
        return f'{self.stream} -- {self.average}'