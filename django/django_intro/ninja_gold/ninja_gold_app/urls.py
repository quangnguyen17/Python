from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money/<str:place>', views.process_money),
    path('process_money/<str:place>/<int:golds>', views.process_money),
]
