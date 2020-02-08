from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>', views.wall),
    path('success/logout', views.log_out),
    path('post_message/<int:user_id>', views.post_message),
    path('delete_message/<int:user_id>', views.delete_message),
    path('post_comment/<int:user_id>', views.post_comment),
    path('delete_comment/<int:user_id>', views.delete_comment),
]
