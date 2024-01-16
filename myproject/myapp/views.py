from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import category, product, order, customer
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

# Create your views here.

def product_detail(request, pk):
    product_instance = product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product_instance})

def home(request):
    products = product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)




def about(request):
    return render(request,'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")    
            return redirect('home') 
        else:
            messages.success(request, "Invalid username or password")    
            return redirect('login')
    else:
        
        return render(request,'login.html', {}) 


def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")    
    return redirect('home') 


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password1']
            
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully registered & logged in")
            return redirect('home')
        else:
            messages.success(request, "Invalid form")    
            return redirect('register')
    else:
            
        return render(request,'register.html', {'form':form})