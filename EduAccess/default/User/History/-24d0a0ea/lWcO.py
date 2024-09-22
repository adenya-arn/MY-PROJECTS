from django.shortcuts import render
from .models import Library, Books
# Create your views here.


def subjects_view(request, *args, **kwargs):
    books = Books.objects.all()

    context = {'books':books}

    return render (request, 'school/subjects_view.html', context)


def subjects_view(request, *args, **kwargs):
    subject = Subjects.objects.all()

    context = {}

    return render (request, 'school/subjects_view.html', context)