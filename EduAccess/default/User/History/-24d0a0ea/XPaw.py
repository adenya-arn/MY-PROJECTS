from django.shortcuts import render
from .models import Library, Book, Request
# Create your views here.

def library_home(request, *args, **kwargs):

    context = {}

    return render (request, 'library/library_home.html', context)


def books_view(request, *args, **kwargs):
    books = Book.objects.all()

    context = {'books':books}

    return render (request, 'library/books_view.html', context)


def libraries_view(request, *args, **kwargs):
    library = Library.objects.all()

    context = {'library':library}

    return render (request, 'library/libraries_view.html', context)


def requests_view(request, *args, **kwargs):
    list = Request.objects.all()

    context = {'list':list}

    return render (request, 'library/requests_view.html', context)