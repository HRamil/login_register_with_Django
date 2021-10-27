from django.shortcuts import redirect, render
from django.contrib.auth import authenticate , login ,logout
from .forms import LoginForm ,  RegisterForm

def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('/') 
    return render(request , 'login.html' , {'form' : form})

def user_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username , password=password)
        login(request,new_user)
        return redirect('/')
    return render(request , 'register.html' , {'form' : form})

def user_logout(request):
    logout(request)
    return redirect('/')

def user_home(request):
     return render(request , 'index.html')