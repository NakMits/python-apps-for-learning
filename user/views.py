from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return redirect('user:signin')


def signin(request):
    def method_get(request_):
        template = 'user/signin.html'
        context = {'msg': ''}
        return render(request, template, context)

    def method_post(request_):
        email = request_.POST['email']
        password = request_.POST['password']
        user = authenticate(request_, username=email, password=password)
        if user:
            login(request_, user)
            return redirect('/admin')
        else:
            context = {'msg': 'メールアドレス もしくは パスワード が一致しません。'}
            template = 'user/signin.html'
            return render(request, template, context)

    if request.method == 'GET':
        return method_get(request)
    elif request.method == 'POST':
        return method_post(request)


def signup(request):
    def method_get(request_):
        template = 'user/signup.html'
        context = {}
        return render(request, template, context)

    def method_post(request_):
        email = request_.POST['email']
        password = request_.POST['password']
        try:
            user = User.objects.create_superuser(email, email, password)
            login(request_, user)
            return redirect('/admin')
        except IntegrityError:
            context = {'msg': f'{email} は既に登録済みです。'}
            template = 'user/signup.html'
            return render(request, template, context)

    if request.method == 'GET':
        return method_get(request)
    elif request.method == 'POST':
        return method_post(request)
