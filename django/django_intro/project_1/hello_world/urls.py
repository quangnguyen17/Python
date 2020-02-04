from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('first-statement/', views.first_statement),
    path('second-statement/', views.second_statement),
]
