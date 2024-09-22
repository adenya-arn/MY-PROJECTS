from django.shortcuts import render
from .models import Library, Books
# Create your views here.


def books_view(request, *args, **kwargs):
    books = Books.objects.all()

    context = {'books':books}

    return render (request, 'library/books_view.html', context)


def libraries_view(request, *args, **kwargs):
    library = Library.objects.all()

    context = {'library':library}

    return render (request, 'library/libraries_view.html', context)