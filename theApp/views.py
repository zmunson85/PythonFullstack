

# Create your views here.

from django.shortcuts import render, redirect
from theApp.models import User, Message, Comment
from django.contrib import messages
import bcrypt
import re



def index(request):
    return render(request, "index.html")


def new_user(request):
    if request.method=="POST":
        errors = User.objects.validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect("/")

    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash
        print(pw_hash)
        User.objects.create(first_name=first_name,
                            last_name=last_name, email=email, password=pw_hash)
        user = User.objects.last()
        request.session['userid'] = user.id
    return redirect('/wall')


def login(request):
    if request.method =="POST":
        errors = User.objects.login_validator(request.POST)

    if errors:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')

    user = User.objects.filter(email=request.POST['email_login'])
    if user:  
        logged_user = user[0]
        print(request.POST['password_login'])
        if bcrypt.checkpw(request.POST['password_login'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/wall')
    messages.error(request, "incorrect password", extra_tags='password_notfound')
    return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')


def wall(request):
    if 'userid' in request.session:
        logged_user = User.objects.get(id=request.session['userid'])
        
        context = {
            'message_wall': Message.objects.all(),
            'logged_user': logged_user,
        }
        return render(request, 'wall.html', context)
    return redirect('/')

def message(request):
    Message.objects.create(message=request.POST['message'], author=User.objects.get(id=request.session['userid']))
    return redirect('/wall')


def comment(request, message_id):
    author = User.objects.get(id=request.session['userid'])
    message = Message.objects.get(id=message_id)
    Comment.objects.create(comment=request.POST['comment'], author=author, message_wall=message)
    return redirect('/wall')


def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect('/wall')
    

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('/wall')
















