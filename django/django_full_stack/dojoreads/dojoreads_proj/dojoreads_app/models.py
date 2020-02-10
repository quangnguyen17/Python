from django.db import models
from login_n_registration_app.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="books",
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(
        Book, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
