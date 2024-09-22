from django.shortcuts import path
from .models import views

urlpatterns =[
    path('', views.hom)
]