from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            User.objects.create_user(username=username,password=password)
            return redirect('userlogin')
    return render(request,"register.html")

def userlogin(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'userlogin.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    return redirect('userlogin')