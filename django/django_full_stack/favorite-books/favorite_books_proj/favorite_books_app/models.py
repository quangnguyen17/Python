from django.db import models
from login_n_registration_app.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(
        User, related_name="books_uploaded", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name="fav_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
