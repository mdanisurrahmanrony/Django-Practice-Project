from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>I am from django_practice_app</h1>")

def contact(request):
    return HttpResponse("<h1>I am from contact page</h1>")
