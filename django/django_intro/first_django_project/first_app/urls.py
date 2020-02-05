from django.urls import path
from . import views

# blogs - update the routes as follows (content is the same):
urlpatterns = [
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy)
]
