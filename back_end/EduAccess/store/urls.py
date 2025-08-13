from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_home, name='store_home'),
    path('items/', views.items_view, name='items'),
    path('stores/', views.stores_view, name='stores'),
]