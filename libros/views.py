from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .services import libros

def index(request):
    return render(request, 'index.html', {})

def base(request):
    return render(request, 'base.html', {})

def listbook(request):
    context= {
        "libros": libros
    }
    return render(request, 'listbook.html', context)