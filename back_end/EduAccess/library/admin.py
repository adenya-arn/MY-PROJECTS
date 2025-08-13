from django.contrib import admin
from .models import Library, Book, Request, Librarian
# Register your models here.

admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Request)
admin.site.register(Librarian)