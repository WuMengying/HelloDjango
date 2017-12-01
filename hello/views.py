from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import User
def home(http):
    users = User.objects.all()
    return render(http,"index.html",{'users':users})

