from django.test import TestCase

# Create your tests here.

# Queries tests
from users_app.models import *

User.objects.create(first_name="Quang", last_name="Nguyen",
                    email="dummy@gmail.com", age=18)
User.objects.create(first_name="Alex", last_name="KFE",
                    email="dummy@gmail.com", age=21)
User.objects.create(first_name="CHris", last_name="Fewewfef",
                    email="dummy@gmail.com", age=34)

User.objects.all()
User.objects.last()
User.objects.first()

user_with_id_3 = User.objects.get(id=3)
user_with_id_3.last_name = "Pancakes"
user_with_id_3.save()

user_with_id_2 = User.objects.get(id=2)
user_with_id_2.delete()

User.objects.all().order_by("first_name")

# BONUS Query: Get all the users, sorted by their first name in descending order
User.objects.all().order_by("-first_name")

# Submit your .txt file that contains all the queries you ran in the shell
