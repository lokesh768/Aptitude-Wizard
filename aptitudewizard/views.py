from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# View : Login
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username Doesn't Exists! (or) Enter Correct Username")
            return redirect('/login/')

        # authentication - checking credentials
        user = authenticate(username=username,password=password)
        if user is None :
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')

    return render(request,'home/login.html')

# View : Logout
def logout_page(request):
    logout(request)
    return redirect('/login/')

# View : Register
def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # checking username is already
        # registered or not 
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username Already taken")
            return redirect('/register/')
        
        # storing user entered details via register form
        # into User model
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Succesfully,Please Login Now!")

        return redirect('/register/')

    return render(request,'home/register.html')

def Home(request):
    return render(request,'home/index1.html')

@login_required(login_url="/login/")
def Quantitative_Aptitude(request):
    return render(request,'home/index2.html')

@login_required(login_url="/login/")
def Logical_Reasoning(request):
    return render(request,'home/index3.html')

@login_required(login_url="/login/")
def Questions(request,category):
    context = {'question':Question.objects.all().filter(category=category)}
    return render(request,'home/questions.html',context)

@login_required(login_url="/login/")
def AddQuestions(request):
    if request.method == "POST":
        data = request.POST
        Question.objects.create(
            category = data.get('category'),
            question = data.get('question'),
            option_1 = data.get('option_1'),
            option_2 = data.get('option_2'),
            option_3 = data.get('option_3'),
            option_4 = data.get('option_4'),
            correct_answer = data.get('correct_answer'),
            solution = data.get('solution')
        )
        return redirect('/add-question/')
    return render(request,'home/addquestion.html')

