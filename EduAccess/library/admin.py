from django.contrib import admin
from .models import Library, Book, Request
# Register your models here.

admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Request)