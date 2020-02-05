from django.urls import path
from . import views

# surveys
urlpatterns = [
    path('', views.surveys),
    path('surveys', views.surveys),
    path('surveys/new', views.surveys_new)
]
