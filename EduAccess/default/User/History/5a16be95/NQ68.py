from django.contrib import admin
from .models import Library, Books, Requests
# Register your models here.

admin.site.register(Library)
admin.site.register(Books)
admin.site.register(Requests)