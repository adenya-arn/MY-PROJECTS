from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items_view, name='items'),
    path('stores/', views.stores_view, name='stores')
]