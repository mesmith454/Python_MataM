from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


# Create your views here.
def base_view(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def greeting(request, name):
    context = {'name': name}
    return render(request, 'base.html', context)