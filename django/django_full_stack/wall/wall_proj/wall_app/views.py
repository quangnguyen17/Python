from django.shortcuts import render, redirect, HttpResponse
from login_n_registration_app.models import *
from .models import *

# Create your views here.


def wall(request, user_id):
    if request.session['user_id'] == user_id:

        context = {
            'user': User.objects.all().get(id=user_id),
            'messages': Message.objects.all().order_by('created_at')
        }

        return render(request, 'wall.html', context)

    return redirect("/")


def log_out(request):
    request.session['user_id'] = None
    return redirect("/")


def post_message(request, user_id):
    Message.objects.create(
        message=request.POST['message'], user=User.objects.all().get(id=user_id))
    return redirect(f"/wall/{user_id}")


def post_comment(request, user_id):
    Comment.objects.create(comment=request.POST['comment'], message=Message.objects.all(
    ).get(id=request.POST['message_id']), user=User.objects.all().get(id=user_id))
    return redirect(f"/wall/{user_id}")


def delete_message(request, user_id):
    Message.objects.all().get(id=request.POST['message_id']).delete()
    return redirect(f"/wall/{user_id}")


def delete_comment(request, user_id):
    Comment.objects.all().get(id=request.POST['comment_id']).delete()
    return redirect(f"/wall/{user_id}")
