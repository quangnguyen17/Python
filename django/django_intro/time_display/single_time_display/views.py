from django.shortcuts import render, HttpResponse, render
from time import gmtime, strftime
import datetime

# Create your views here.


def index(request):
    return HttpResponse("Getting a response.")


def display_time(request):
    custom_datetime = datetime.datetime.now()

    context = {
        "time_1": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "time_2": custom_datetime,
        "year": custom_datetime.year,
        "month": custom_datetime.strftime("%B"),
        "day": custom_datetime.strftime("%A"),
        "date": custom_datetime.strftime("%d")
    }

    return render(request, "index.html", context)
