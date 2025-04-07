from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

import users.forms as forms


# Create your views here.

def register_user(request):
    if request.POST:
        form = forms.RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Siz ro'yhatdan o'tdingiz")
            return redirect("/")
    form = forms.RegisterUser()
    return render(request,
                  "auth/register.html",
                  {"form": form})


def login_user(request):
    if request.POST:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Xush kelibsiz")
                return redirect("/")
        else:
            messages.error(request, f"Username yoki Password xato !")

    form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.info(request, "Xayr")
    return redirect("/")
