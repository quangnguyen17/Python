from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('random_world', views.random_world),
    path('random_world/reset', views.reset)
]
