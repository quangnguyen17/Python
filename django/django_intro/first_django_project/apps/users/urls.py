from django.urls import path
from . import views

# users
urlpatterns = [
    path('', views.users),
    path('register', views.register),
    path('login', views.login),
    path('users/new', views.users_new),
    path('users', views.users),
]
