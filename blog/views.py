from django.shortcuts import render
from .models import Posts


def home(request):
    io = Posts.objects
    return render(request, 'home.html',{'io':io})

