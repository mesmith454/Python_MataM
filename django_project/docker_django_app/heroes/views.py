from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def heroes(request):
    return HttpResponse("I'm gonna be a list of heroes.")