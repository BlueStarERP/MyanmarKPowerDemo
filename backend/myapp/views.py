import datetime

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView,ListView
# import generic UpdateView
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('myapp:home')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('myapp:home')
            else:
                messages.info(request, 'username or password invalid')
            # return render(request, 'login.html', context)
        context ={}
        return render(request, 'shop/login.html', context)

@login_required(login_url='myapp:login')
def home(request):
    try:
        p = StaffPermission.objects.get(usr = request.user)
        # print(p.hr)
        if p.manager is True:
            return render(request, 'shop/dashboard.html')
        
        elif p.admin is True:
            print('Admin')
        elif p.supervisor is True:
            print('Supervisor')
        else:    
            return render(request, 'shop/dashboard.html')
    except StaffPermission.DoesNotExist:
        # return HttpResponse('hellllo')
        return redirect('myapp:login')


def create_item(request):
    fm = ItemsForm()
    context = {'fm':fm}
    return render(request, 'shop/create_item.html',context)

def category_list(request):
    context = {}
    return render(request, 'shop/category_list.html',context)

def item_details(request):
    context = {}
    return render(request, 'shop/item_details.html',context)


# SHOP
def shopview1(request):
    context = {}
    return render(request, 'shopview1.html',context)
    
def shopview2(request):
    context = {}
    return render(request, 'shopview2.html',context)