from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from users.signup_form import SignupForm
from django.contrib.auth.models import User
from users.login_form import LoginForm

# Create your views here.

def login_view(request):
    if request.method == "POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            print(login_form.cleaned_data)
            # username=request.POST['username']
            # password=request.POST['password']
            # user=authenticate(username=username,password=password)
            # print(user)
            # if user:
            #     login(request,user)
            #     return redirect('index')
            # else:
            #     context = {'error':'Invalid Username or Password!!'}
            #     return render(request, 'login.html',context)
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('index')
            else:
                login_form.add_error(user,'Username or Password is incorrect!!')
                return render(request,'login.html',{'login_form':login_form})


    login_form=LoginForm()
    context={'login_form':login_form}
    return render(request,'login.html',context) 

def signup(request):
    if request.method == 'POST':
        signup_form=SignupForm(request.POST)
        if signup_form.is_valid(): 
            user = signup_form.save()
            user.refresh_from_db()
            user.save()
            return redirect('index')
        else:
            signup_form=SignupForm()
            return render(request,'signup.html',{'signup_form':signup_form})
        
    signup_form=SignupForm()
    return render(request,'signup.html',{'signup_form':signup_form})
