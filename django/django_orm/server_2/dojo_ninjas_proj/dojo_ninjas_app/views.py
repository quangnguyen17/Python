from django.shortcuts import render, HttpResponse
from .models import Dojo, Ninja

# Create your views here.


def index(request):
    # Put in to a real function
    Dojo.objects.create(name="Orange County", city="Costa Mesa", state="CA")
    Dojo.objects.create(name="Los Angeles", city="Burbank", state="CA")
    Dojo.objects.create(name="Silicon Valley", city="San Jose", state="CA")

    Dojo.objects.get(id=1).delete()
    Dojo.objects.get(id=2).delete()
    Dojo.objects.get(id=3).delete()

    Dojo.objects.create(name="Orange County", city="Costa Mesa", state="CA")
    Dojo.objects.create(name="Los Angeles", city="Burbank", state="CA")
    Dojo.objects.create(name="Silicon Valley", city="San Jose", state="CA")

    Ninja.objects.create(
        first_name="First", last_name="First", dojo=Dojo.objects.get(id=1)
    )
    Ninja.objects.create(
        first_name="First", last_name="First", dojo=Dojo.objects.get(id=1)
    )
    Ninja.objects.create(
        first_name="First", last_name="First", dojo=Dojo.objects.get(id=1)
    )

    Ninja.objects.create(
        first_name="Second", last_name="Second", dojo=Dojo.objects.get(id=2)
    )
    Ninja.objects.create(
        first_name="Second", last_name="Second", dojo=Dojo.objects.get(id=2)
    )
    Ninja.objects.create(
        first_name="Second", last_name="Second", dojo=Dojo.objects.get(id=2)
    )

    Ninja.objects.create(
        first_name="Third", last_name="Third", dojo=Dojo.objects.get(id=3)
    )
    Ninja.objects.create(
        first_name="Third", last_name="Third", dojo=Dojo.objects.get(id=3)
    )
    Ninja.objects.create(
        first_name="Third", last_name="Third", dojo=Dojo.objects.get(id=3)
    )

    Dojo.objects.first().ninjas
    Dojo.objects.last().ninjas

    # Retrieve the last ninja's dojo
    Dojo.objecst.last().ninja

    return HttpResponse("Responded.")

