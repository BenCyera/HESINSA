from django.shortcuts import render, redirect
from .forms import UserModel
from django.contrib.auth import get_user_model, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def sign_up_view(request):
    if request.method == 'POST':
        form = UserModel(request.POST)
        print(form.errors)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('/index')

    elif request.method == 'GET':
        form = UserModel()
    return render(request, 'user/signup.html', {'form': form})


# # 준열님꺼 -----
#     if request.method == 'POST':
#         form = UserModel(request.POST)
#         print(form.errors)
#         print(form)
#         # 유효성 검사
#         if form.is_valid():
#             user = form.save()
#             # 회원가입 후 로그인 상태로 만들어줌
#             login(request, user)
#             return redirect('/product-list')
#
#     elif request.method == 'GET':
#         # user가 로그인 상태면 다시 홈으로 보냄
#         user = request.user.is_authenticated
#         if user:
#             return redirect('/product-list')
#         else:
#             form = UserModel()
#     return render(request, 'user/signup.html', {'form': form})


# def sign_in_view(request):
#     if request.method == 'POST':
#         form = UserModel(request.POST)
#         if form.is_valid():


# Create your views here.
# def sign_up_view(request):
#     if request.method == 'GET':
#         user = request.user.is_authenticated
#         if user:
#             return redirect('/')
#         else:
#             return render(request, 'user/signup.html')
#     elif request.method == 'POST':
#         # username = request.POST.get('username', None)
#         # password = request.POST.get('password', None)
#         # password2 = request.POST.get('password2', None)
#         # bio = request.POST.get('bio', None)
#         form = UserModel(request.POST)
#
#         if password != password2:
#             return render(request, 'user/signup.html')
#         else:
#             exist_user = get_user_model().objects.filter(username=username)
#             if exist_user:
#                 return render(request, 'user/signup.html')
#             else:
#                 UserModel.objects.create_user(username=username, password=password, bio=bio)
#             return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            print(me)
            return redirect("/index")
        else:
            return redirect("/sign-in")

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/index')

    return render(request, 'user/signin.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/sign-in')
