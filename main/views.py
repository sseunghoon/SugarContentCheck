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
        'questions': questions,
        'questions_count': questions_count,
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
    intensity_sum = 0

    for i in range(1, question_cnt+1):
        intensity = int(request.POST[f'question-{i}'])
        intensity_sum = intensity_sum + intensity

    serial_num = int(request.POST[f'serial_num'])
    belong = int(request.POST[f'belong'])

    result = Result()
    result.intensity_sum = intensity_sum
    result.serial_num = serial_num
    result.belong = belong
    result.save()

    #####################################################

    result_cnt = Result.objects.count()
    results = Result.objects.all()
    result_low_cnt = 0

    for r in results:
        if(r.intensity_sum <= intensity_sum):
            result_low_cnt += 1

    result_high_cnt = result_cnt - result_low_cnt

    rank = result_high_cnt+1
    percentage = round(rank / result_cnt * 100, 2)

    if(percentage <= 50):
        isTop = 1
    else:
        isTop = 0
        percentage = 100-percentage

    #####################################################

    belongResult_cnt = Result.objects.count()
    belongResults = Result.objects.all()
    belongResult_low_cnt = 0

    for br in belongResults:
        if(br.intensity_sum <= intensity_sum):
            belongResult_low_cnt += 1
    
    belongResult_high_cnt = belongResult_cnt - belongResult_low_cnt

    belongRank = belongResult_high_cnt + 1
    belongPercentage = round(belongRank / belongResult_cnt * 100, 2)

    if(belongPercentage <= 50):
        belongIsTop = 1
    else:
        belongIsTop = 0
        belongPercentage = 100-belongPercentage

    #####################################################

    serialResult_cnt = Result.objects.count()
    serialResults = Result.objects.all()
    serialResult_low_cnt = 0

    for sr in serialResults:
        if(sr.intensity_sum <= intensity_sum):
            serialResult_low_cnt += 1

    serialResult_high_cnt = serialResult_cnt - serialResult_low_cnt

    serialRank = serialResult_high_cnt + 1
    serialPercentage = round(serialRank / serialResult_cnt * 100, 2)

    if(serialPercentage <= 50):
        serialIsTop = 1
    else:
        serialIsTop = 0
        serialPercentage = 100-serialPercentage

    if(belong == 1):
        belong_str = "육군"
    elif(belong == 2):
        belong_str = "해군"
    else:
        belong_str = "공군"

    serial_str = str(serial_num)+"군번"

    #####################################################

    context = {
        'intensity_sum': intensity_sum,
        'result_cnt': result_cnt,
        'percentage': percentage,
        'rank': rank,
        'isTop': isTop,
        'belong': belong,
        'belongResult_cnt': belongResult_cnt,
        'belongPercentage': belongPercentage,
        'belongRank': belongRank,
        'belongIsTop': belongIsTop,
        'serial_num': serial_num,
        'serialResult_cnt': serialResult_cnt,
        'serialPercentage': serialPercentage,
        'serialRank': serialRank,
        'serialIsTop': serialIsTop,
        'belong_str': belong_str,
        'serial_str': serial_str,
    }

    return render(request, 'result.html', context)






