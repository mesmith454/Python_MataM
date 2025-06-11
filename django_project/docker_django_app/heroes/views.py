from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Hero
# Create your views here.

def heroes(request):
    myheroes = Hero.objects.all().values()
    template = loader.get_template('all_heroes.html')
    context = {
        'myheroes': myheroes,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    myhero = Hero.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'myhero': myhero,
    }
    return HttpResponse(template.render(context, request))