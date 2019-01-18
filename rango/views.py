from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Rango says hey there partner! Here is a link ' + '<a href="/rango/about/">About</a>')

def about(request):
    return HttpResponse('Rango says here is the about page and here is a link back ' + '<a href="/rango/">Home</a>')
