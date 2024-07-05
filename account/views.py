from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User
from .forms import CustomUserCreateForm
from django.contrib.auth.decorators import login_required


def create(request):
    if request.method == 'GET':
        return render(
            request, 
            "account/create.html", 
            {"form":CustomUserCreateForm()}
        )
    elif request.method == "POST":
        form = CustomUserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('home'))
        else:
            return render(request, "account/create.html",
                        {"form":form})
        
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm 
def user_login(request):
    if request.method == "GET":
        return render(request, 
                    'account/login.html', 
                    {"form":AuthenticationForm()})
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("home"))
        else:
            return render(
                request,
                'account/login.html', 
                {"form":AuthenticationForm(), 
                "errorMessage":"ID나 Password를 다시 확인하세요."})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('home'))