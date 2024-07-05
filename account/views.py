from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User
from .forms import CustomUserCreateForm
from django.contrib.auth.decorators import login_required


def create(request):
    if request.method == 'GET':
        # context data 로 빈 Form(ModelForm) 객체를 template 전달.
        return render(
            request, 
            "account/create.html", 
            {"form":CustomUserCreateForm()}
        )
    elif request.method == "POST":
        # 요청파라미터 조회 -> 검증
        ### ModelForm/Form 에 요청파라미터를 넣어서 객체 생성.
        form = CustomUserCreateForm(request.POST, request.FILES)
        ## 검증 결과 이상이 없으면
        if form.is_valid():
            #정상처리 -> DB 저장 (ModelForm.save(): Model)
            user = form.save() # insert하고 insert한 값들을 가진 User(Model)객체를 반환
            # 응답 : 등록->redirect방식
            return redirect(reverse('home'))
        else:
            # 요청파라미터 검증 실패. => 등록폼으로 이동.
            return render(request, "account/create.html",
                        {"form":form})  # form: 요청파라미터를 가진 Form

from django.contrib.auth import login, logout, authenticate       
# login(), logout(): 로그인/로그아웃 처리하는 함수
# authenticate(): username/password를 확인함수.
from django.contrib.auth.forms import AuthenticationForm 
#로그인 모델폼 - username, password 입력폼

### 로그인 처리: GET-로그인 폼반환, POST-로그인 처리
def user_login(request):
    if request.method == "GET":
        return render(request, 
                    'account/login.html', 
                    {"form":AuthenticationForm()})
    elif request.method == "POST":
        # 요청파라미터 조회
        username = request.POST['username']
        password = request.POST['password']
        ## AUTH_USER_MODEL를 기반으로 사용자 인증 처리
        ### 받은 username/password가 유효한 사용자 계정이라면 User객체를 반환.
        ###      유효하지 않은 사용자 계정이라면 None 반환.
        user = authenticate(request, username=username, password=password)
        if user is not None: # 유효한 사용자 계정.
            login(request, user) # 로그인 처리 -> 로그아웃할 때까지 request에 로그인한 사용자 정보를 사용할 수있도록 처리.
            return redirect(reverse("home"))
        else: # 유효한 사용자 계정이 아님
            return render(
                request,
                'account/login.html', 
                {"form":AuthenticationForm(), 
                "errorMessage":"ID나 Password를 다시 확인하세요."})

### 로그아웃 처리
@login_required  # view를 실행할 때 로그인 되었는지를 먼저 체크한다
# 로그인이 안되어있으면 LOGIN_URL로 이동함
def user_logout(request):
    # login() 시 처리한 것들을 다 무효화시킴
    logout(request)
    return redirect(reverse('home'))

##### 로그인한 사용자 정보 조회
def user_detail(request):
    ## 로그인한 사용자 정보 -> request.user
    user = User.objects.get(pk=request.user.pk)
    return render(request, "account/detail.html", {"object":user})
