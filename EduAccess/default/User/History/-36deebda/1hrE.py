from django.urls import path
from . import views

urlpatterns = [
    path('requests/', views.requests_view, name='requests'),
    path('books/', views.books_view, name='books'),
    path('libraries/', views.libraries_view, name='libraries'),
]