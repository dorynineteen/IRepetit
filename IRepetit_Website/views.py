from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def index(request):
    return render(request, 'IRepetit_Website/index.html')


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print(form)
            return redirect('/IRepetit/index')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'IRepetit_Website/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print(form)
            return redirect('/IRepetit/')
        else:
            print(form.errors)
    form = AuthenticationForm()
    return render(request, 'IRepetit_Website/login.html', {'form': form})


def user_profile(request):
    return render(request, 'IRepetit_Website/profile.html', {'user': request.user})


def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/IRepetit/")


def tutor(request):
    return render(request, 'IRepetit_Website/tutor.html')
