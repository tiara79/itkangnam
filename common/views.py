# ----------------- [edit - 21/04/19]  로그아웃 -----------------
from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth import authenticate, login

from common.forms import UserForm

def logout(request):
    auth.logout(request)
    # 로그아웃시 메인(index)으로 리턴
    return redirect('newapp:infoIndex')

# ----------------- [21/04/19]  회원가입 함수 생성 -----------------
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# [21/04/27] 회원 가입 페이지 생성
def agree(request):
    return render(request, 'common/agree.html')

# [21/04/27] 서비스 게시판 페이지 생성
def service(request):
    return render(request, 'common/service.html')

# Create your views here.
