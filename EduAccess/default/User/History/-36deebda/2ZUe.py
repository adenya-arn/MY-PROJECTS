from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_view, name='books'),
    path('libraries/', views.libraries_view, name='libraries'),
]