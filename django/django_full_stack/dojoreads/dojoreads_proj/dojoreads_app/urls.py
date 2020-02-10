from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>', views.books),
    path('<int:user_id>/<int:book_id>', views.book_preview),
    path('<int:user_id>/add', views.add_book_and_review),
    path('<int:user_id>/handle_adding', views.handle_adding),
    path('<int:user_id>/review', views.user_review),
    path('<int:user_id>/add_review', views.add_review),
    path('<int:user_id>/<int:review_id>/remove_review', views.remove_review),
    path('logout', views.logout),
]
