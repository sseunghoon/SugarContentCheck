from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Result, Choice

def index(request):
    context={}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
    
    