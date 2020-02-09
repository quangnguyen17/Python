from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.


def index(request):
    if 'user_id' in request.session:
        if request.session['user_id'] != None:
            return redirect(f"/books/{request.session['user_id']}")
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def log_in(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        return render(request, 'index.html', {'messages': errors.values()})
    else:
        for user in User.objects.all():
            password_matched = bcrypt.checkpw(
                request.POST['password'].encode(), user.password.encode())
            email_matched = user.email == request.POST['email']
            if password_matched and email_matched:
                request.session['user_id'] = user.id
                return redirect("/")

        return redirect("/", {'messages': ['Passwords and Emails do not match.']})


def log_out(request):
    request.session['user_id'] = None
    return redirect("/")


def register(request):
    errors = User.objects.register_validator(request.POST)

    if len(errors) > 0:
        return render(request, 'index.html', {'messages': errors.values()})
    else:
        password = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], birthdate=request.POST['birthdate'], email=request.POST['email'], password=password)
        request.session['user_id'] = user.id
        return redirect(f"/books/{user.id}")


def success(request, user_id):
    if request.session['user_id'] == user_id:
        context = {
            'user': User.objects.all().get(id=user_id)
        }
        return redirect(f"/books/{user.id}", context)
    else:
        return redirect("/")
