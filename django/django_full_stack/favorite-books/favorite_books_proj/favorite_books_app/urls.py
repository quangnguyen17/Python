from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>', views.index),
    path('<int:user_id>/upload', views.upload_book),
    path('preview/<int:user_id>/<int:book_id>', views.book_preview),
    path('<int:user_id>/<int:book_id>/favorite', views.favorite),
    path('preview/favorite', views.favorite_2),
    path('<int:user_id>/update/book', views.update),
    path('logout', views.log_out),
]
