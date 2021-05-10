from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Result, Choice
from django.urls import reverse

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
    questions_count = Question.objects.count()
    
    context = {
        'questions':questions,
        'questions_count':questions_count,
    }
    return render(request, 'form.html', context)

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     selected_choice.votes += 1
#     selected_choice.save()
#     # POST data가 잘 처리되었으면 언제나 HttpResponseRedirect를 줘서
#     # 유저가 뒤로 가기 버튼을 눌렀을 때 2번 전송되는 것을 방지함
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def result(request):
    question_cnt = Question.objects.count()
    intensity_sum=0
    
    
    for i in range(1, question_cnt+1):
        intensity = int(request.POST[f'question-{i}'])
        intensity_sum = intensity_sum + intensity

    serial_num = int(request.POST[f'serial_num'])
    belong = int(request.POST[f'belong'])
        
    result=Result()
    result.intensity_sum = intensity_sum
    result.serial_num=serial_num
    result.belong=belong
    result.save()
        
    context = {
        'intensity_sum': intensity_sum,
    }

    # return render(request, 'result.html', context)
    return HttpResponseRedirect(reverse('main:result', args=(str(intensity_sum))))






