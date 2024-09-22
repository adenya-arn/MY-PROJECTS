from django.contrib import admin
from .models import Parents, Students, Subjects, Ids, Grades, Classes

# Register your models here.

admin.site.register(Parents)
admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(Ids)
admin.site.register(Grades)
admin.site.register(Classes)