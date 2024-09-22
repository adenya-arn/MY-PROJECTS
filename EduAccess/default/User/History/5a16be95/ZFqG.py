from django.contrib import admin
from .models import Library, Books
# Register your models here.

admin.site.register(Library)
admin.site.register(Books)