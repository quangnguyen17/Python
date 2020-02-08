from django.db import models
from login_n_registration_app.models import User
from datetime import datetime
# Create your models here.


class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(
        User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def first_30_mins(self):
        now = int(datetime.now().strftime("%-M"))
        created = int(self.created_at.strftime("%-M"))

        calc = created + 30
        if calc > 60:
            now += 60

        return now > calc


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(
        Message, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
