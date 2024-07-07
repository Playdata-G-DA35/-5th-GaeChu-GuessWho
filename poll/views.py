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
    ans_list = Ans_vote.objects.filter(img_path = i)
    #c = Category(c = i.category)

    return render(request, "poll/ans_vote.html", {'category_id': category_id, 'img_name': i.img_name, 'ans_list': ans_list})

def ans_create(request, category_id, img_name):
    i = Image_path.objects.get(img_name=img_name, category=category_id)

    if request.method == 'POST':
        user = request.user
        comment = request.POST.get('content')
        if comment:  # comment가 비어 있지 않은지 확인
            #Ans_vote.objects.create(img_path=i, ans_text=comment, votes=0)
            ans = Ans_vote(img_path= i, ans_text= comment, votes= 0)
            ans.save()

    return redirect('poll:ans_vote', category_id=category_id, img_name=img_name)