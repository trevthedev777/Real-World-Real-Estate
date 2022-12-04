from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),  # Login page
    path('register', views.register,
         name='register'),  # listing page
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
