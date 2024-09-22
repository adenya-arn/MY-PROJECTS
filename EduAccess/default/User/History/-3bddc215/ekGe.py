from django.db import models

# Create your models here.


class Ids (models.Model):
    id_no = models.BigIntegerField()
    name = models.CharField(max_length=100)
    position = models.OneToOneField(Position, on_delete=models.PROTECT)    

class Students (models.Model):
    pass

class Classes (models.Model):
    pass

class Grades (models.Model):
    pass

class Subjects (models.Model):
    pass

class Parents (models.Model):
    pass