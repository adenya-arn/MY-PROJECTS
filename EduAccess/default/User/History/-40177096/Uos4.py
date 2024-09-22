from django.contrib import admin
from .models import Parent, Student,Subject, Staff, Grade, Class, Role, Performance

# Register your models here.

admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Staff)
admin.site.register(Grade)
admin.site.register(Class)
admin.site.register(Role)
admin.site.register(Performance)