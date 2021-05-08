from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Result, Choice

def index(request):
    total_num = Result.objects.count()
    army_num = Result.objects.filter(serial_num=0).count()
    navy_num = Result.objects.filter(serial_num=1).count()
    airforce_num = Result.objects.filter(serial_num=2).count()
    
    context = {
        'total_num': total_num,
        'army_num': army_num,
        'navy_num': navy_num,
        'airforce_num': airforce_num,
    }
    return render(request, 'index.html', context)

def form(request):
    questions = Question.objects.all()
    questions_count = Question.objects.all().count()
    
    context = {
        'questions':questions,
        'questions_count':questions_count,
    }
    return render(request, 'form.html', context)