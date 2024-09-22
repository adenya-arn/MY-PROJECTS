from django.contrib import admin
from .models import Parents, Students,Subjects, Staff, Grades, Classes, Roles, Performance

# Register your models here.

admin.site.register(Parents)
admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(Staff)
admin.site.register(Grades)
admin.site.register(Classes)
admin.site.register(Roles)