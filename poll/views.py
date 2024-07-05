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

def ans_vote(request, category_id, img_name):
    i = Image_path.objects.get(img_name=img_name, category=category_id)
    #c = Category(c = i.category)

    return render(request, "poll/ans_vote.html", {'cid_of_views': category_id, 'img_path': i.img_path})

#def create_ans_vote(request):
#    ans_vote = Ans_vote()