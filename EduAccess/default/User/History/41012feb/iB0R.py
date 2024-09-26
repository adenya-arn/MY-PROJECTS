from django.shortcuts import render, redirect
from .models import Staff, Student, Class, Grade, Subject, Parent, Role, Performance
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/home_view.html', context)


def classes_view(request, *args, **kwargs):
    classes = Class.objects.all()

    context = {'classes':classes}

    return render (request, 'school/classes_view.html', context)



def grade_view(request, *args, **kwargs):
    grade = Grade.objects.all()

    context = {'grade':grade}

    return render (request, 'school/grade_view.html', context)



def parents_view(request, *args, **kwargs):
    parents = Parent.objects.get

    context = {'parents':parents}

    return render (request, 'school/parents_view.html', context)



def roles_view(request, *args, **kwargs):
    roles = Role.objects.all()

    context = {'roles':roles}

    return render (request, 'school/roles_view.html', context)



def staff_view(request, *args, **kwargs):
    staff = Staff.objects.all()

    context = {'staff':staff}

    return render (request, 'school/staff_view.html', context)


def students_view(request, *args, **kwargs):
    students = Student.objects.all()

    context = {'students':students}

    return render (request, 'school/students_view.html', context)



def subjects_view(request, *args, **kwargs):
    subject = Subject.objects.all()

    context = {}

    return render (request, 'school/subjects_view.html', context)


def login_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/login_view.html', context)


def logout_view(request, *args, **kwargs):

    context = {}

    return render (request, 'school/logout_view.html', context)


def register_view(request, *args, **kwargs):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}

    return render (request, 'school/register_view.html', context)


def performance_view(request, *args, **kwargs):
    average = Performance.objects.all()

    context = {}

    return render (request, 'school/performance_view.html', context)

