from django.contrib import admin
from .models import Parent, Student,Subject, Staff, Grade, Class, Role, Performance, Stream
from . models import User, UserManager

from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
# Register your models here.

admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Staff)
admin.site.register(Grade)
admin.site.register(Class)
admin.site.register(Role)
admin.site.register(Performance)
admin.site.register(Stream)

class UserAdmin(CustomUserAdmin):
    list_dispaly = ('email',)
    #only email will show up on the admin site ....

admin.site.register(User, UserAdmin)