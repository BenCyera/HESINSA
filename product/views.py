from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import ProductForm
# from django.contrib.auth import
# from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Product


# 홈
@login_required
def index_view(request):
    if request.method == 'GET':
        product = Product.objects.filter(~Q(size='F'), inventory__gt=0).order_by('code', '-size')
        product_free = Product.objects.filter(inventory__gt=0, size='F').order_by('code')
        return render(request, 'product/index.html', {'product': product, 'product_free': product_free})


# 재고 현황
@login_required
def cont_view(request):
    if request.method == 'GET':
        product = Product.objects.filter(~Q(size='F')).order_by('code', '-size')
        product_free = Product.objects.filter(size='F').order_by('code')
        return render(request, 'product/container.html', {'product': product, 'product_free': product_free})


# 입고 렌더
def input_view(request):
    select_hood = []
    select_free = []
    if request.method == 'POST':
        select = request.POST.getlist('data_1')
        select_hood = Product.objects.filter(pk__in=select)
        select_2 = request.POST.getlist('data_2')
        select_free = Product.objects.filter(pk__in=select_2)
    if request.method == 'GET':
        return render(request, 'product/input.html', {'select_hood': select_hood, 'select_free': select_free})





# 출고
def output_view(request):
    return render(request, 'product/output.html')
