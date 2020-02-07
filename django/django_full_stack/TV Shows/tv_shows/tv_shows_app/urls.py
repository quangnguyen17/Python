from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/new/add', views.add_show),
    path('shows/<int:id>', views.shows_id),
    path('shows/<int:id>/edit', views.shows_edit),
    path('shows/<int:id>/delete', views.delete_show),
    path('shows/<int:id>/save', views.save_edit)
]
