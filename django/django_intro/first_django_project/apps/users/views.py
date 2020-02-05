from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def register(request):
    return HttpResponse("placeholder for users to create a new user record")


def login(request):
    return HttpResponse("placeholder for users to log in")


def users_new(request):
    print("users_new: handling request")
    return redirect("/regieter")


def users(request):
    return HttpResponse("placeholder to later display all the list of users")
