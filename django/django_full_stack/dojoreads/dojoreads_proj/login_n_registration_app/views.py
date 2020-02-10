from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.views.generic import View
from .models import User
import bcrypt


class LoginRegistration(View):
    def get(self, request):
        return redirect("/")

    def post(self, request):
        if 'register' in request.POST:
            errors = User.objects.register_validator(request.POST)
            password = bcrypt.hashpw(
                request.POST['password'].encode(), bcrypt.gensalt()).decode()

            if len(errors) > 0:
                return render(request, 'index.html', {'messages': errors.values()})

            user = User.objects.create(
                first_name=request.POST['first_name'], last_name=request.POST['last_name'], birthdate=request.POST['birthdate'], email=request.POST['email'], password=password)
            request.session['user_id'] = user.id
            return redirect("/")

        if 'login' in request.POST:
            errors = User.objects.login_validator(request.POST)
            if len(errors) > 0:
                return render(request, 'index.html', {'messages': errors.values()})

            for user in User.objects.all():
                password_matched = bcrypt.checkpw(
                    request.POST['password'].encode(), user.password.encode())
                print(user.password)
                if password_matched and (user.email == request.POST['email']):
                    request.session['user_id'] = user.id
                    return redirect("/")

            return redirect("/", {'messages': ['Passwords and Emails do not match.']})

        return redirect("/")


def index(request):
    if 'user_id' in request.session:
        if request.session['user_id'] != None:
            return redirect(f"/books/{request.session['user_id']}")
        return render(request, 'index.html')
    return render(request, 'index.html')


def log_out(request):
    request.session['user_id'] = None
    return redirect("/")


def success(request, user_id):
    context = {'user': User.objects.all().get(id=user_id)}
    return redirect(f"/books/{user_id}") if request.session['user_id'] == user_id else redirect("/")
