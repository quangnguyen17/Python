from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('hello/<str:name>', views.hello),
    path('<int:number>', views.show),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy),
    path('delete/<int:id>', views.delete)
]
