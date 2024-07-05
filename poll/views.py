from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def cat_list(request):
    """
    질문 리스트 보여주기
    """
    category_list = Category.objects.all().order_by('-pub_date')
    return render(request, 'poll/cat_list.html', {"category_list": category_list})

def img_list(request, category_id):
    try:
        c = Category(pk=category_id)
        image_list = Image_path.objects.filter(category = c)
        return render(request, "poll/img_list.html", {"category_id": category_id, "image_list": image_list})
    except:
        print("없는 질문을 요청했습니다")

def ans_vote(request, img_path):
    return render(request, "poll/ans_vote.html", {'img_path': img_path})