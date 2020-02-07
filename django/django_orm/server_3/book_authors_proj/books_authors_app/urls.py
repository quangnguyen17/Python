from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('books', views.home),
    path('authors', views.authors),
    path('book/add', views.add_book),
    path('book/<int:id>/remove', views.remove_book),
    path('book/<int:id>', views.book),
    path('author/<int:id>', views.author),
    path('author/add', views.add_author),
    path('author/<int:id>/remove', views.remove_author),
    path('author/add_to_book/<int:book_id>', views.add_author_to_book),
    path('book/add_to_author/<int:author_id>', views.add_book_to_author)
]
