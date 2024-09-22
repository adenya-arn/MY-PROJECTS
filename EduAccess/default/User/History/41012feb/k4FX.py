from django.shortcuts import render
from .models import Staff, Students, Classes, Grades, Subjects, Parents, Roles

# Create your views here.

def home_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/home_view.html', context)


def classes_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/home_view.html', context)



def grade_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/home_view.html', context)



def parents_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/home_view.html', context)



def roles_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/home_view.html', context)



def staff_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/home_view.html', context)


def students_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/home_view.html', context)



def subjects_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/home_view.html', context)




