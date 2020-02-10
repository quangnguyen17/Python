from django.urls import path
from . import views
from login_n_registration_app.views import LoginRegistration

urlpatterns = [
    path('', views.index),
    path('login', LoginRegistration.as_view()),
    path('register', LoginRegistration.as_view()),
    path('success/logout', views.log_out, name="logout"),
    path('success/<int:user_id>', views.success)
]
