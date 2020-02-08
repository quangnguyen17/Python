from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.log_in),
    path('success/logout', views.log_out),
    path('register', views.register),
    path('success/<int:user_id>', views.success)
]
