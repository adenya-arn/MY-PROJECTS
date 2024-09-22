from django.urls import path
from . import views

urlpatterns =[
    path('', views.home_view, name='home'),
    path('classes/', views.classes_view, name='classes'),
    path('grades/', views.grade_view, name='grade'),
    path('parents/', views.parents_view, name='parents'),
    path('roles/', views.roles_view, name='roles'),
    path('staff/', views.staff_view, name='staff'),
    path('students/', views.students_view, name='students'),
    path('subjects/', views.subjects_view, name='subjects'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('performance/', views.performance_view, name='performance'),
]