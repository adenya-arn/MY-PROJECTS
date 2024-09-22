from django.db import models

# Create your models here.

class Roles (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Staff (models.Model):
    id_no = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    position = models.OneToOneField(Roles, on_delete=models.PROTECT)  

    def ___str__(self):
        return f'ID -- {self.id_no} -- name {self.name} -- {self.position}'  


class Classes (models.Model):
    number = models.SmallIntegerField()
    stream = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.number}{self.stream}'

class Grades (models.Model):
    marks = models.SmallIntegerField()
    grade = models.CharField(max_length=10)
    student = models.ForeignKey('Students', on_delete=models.PROTECT, related_name='student') 

    def __str__ (self):
        return f'{self.student} {self.grade}'


class Subjects (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Parents (models.Model):
    id_no = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    child = models.ManyToManyField('Students')

    def __str__(self):
        return self.name


class Students (models.Model):
    reg_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    stream = models.ForeignKey(Classes, on_delete=models.PROTECT, related_name='classes')
    parent = models.OneToOneField(Parents, on_delete=models.PROTECT, related_name='children')
    results = models.ForeignKey(Grades, on_delete=models.CASCADE, related_name='grades')
    subjects = models.ForeignKey(Subjects, on_delete=models.SET_NULL, related_name='subjects', null=True)

    def __str__(self):
        return f'{self.name} -- {self.reg_no}'
    

class Performance (models.Model):
    stream = models.CharField(max_length=100, blank=True, null=True)
    average = models.SmallIntegerField()


    def __str__ (self):
        return f'{self.stream} -- {self.average}'