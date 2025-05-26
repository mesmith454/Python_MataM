from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import NameForm

# Create your views here.
def base_view(request):

    template = loader.get_template('base.html')
    return HttpResponse(template.render())

