from django.shortcuts import render
from .models import Staff, Students, Classes, Grades, Subjects, Parents, Roles

# Create your views here.

def home_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/home_view.html', context)