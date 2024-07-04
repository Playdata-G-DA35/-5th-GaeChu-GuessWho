from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def hello(request):
    return HttpResponse("안녕하세요!")

# def list(request):
#     question_list = Question.objects.all().order_by('-pub_date')
#     return render(
#         request, "poll/list.html",
#         {"question_list":question_list},
#     )

def list(request):
    """
    질문 리스트 보여주기
    """
    question_list = Question.objects.all().order_by('-pub_date')
    return render(request, 'poll/list.html', {"question_list": question_list})

def img_list(request, category_id):
    try:
        # question = Question.objects.get(pk=category_id)
        return render(request, "poll/img_list.html", {"category_id": category_id})
    except:
        print("없는 질문을 요청했습니다")

def ans_vote(request):
    return render(request, "poll/ans_vote.html")