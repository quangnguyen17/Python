from django.shortcuts import render, HttpResponse

# Create your views here.


def surveys(request):
    return HttpResponse("placeholder to display all the surveys created")


def surveys_new(request):
    return HttpResponse("placeholder for users to add a new survey")
