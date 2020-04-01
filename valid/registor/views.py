from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def registor(response):
    form = UserCreationForm()
    return render(response,"templates/register.html",{"form":form})

