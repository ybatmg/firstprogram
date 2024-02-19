from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    return render(request,'signup.html')

def login_view(request):
    if request.method == "POST":
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            print(user)
            if user:
                login(request,user)
                return redirect('index')
            else:
                context = {'error':'Invalid Username or Password!!'}
                return render(request, 'login.html',context)
    return render(request,'login.html') 

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['username']
        user = User.objects.create_user(username,email,password)
        print(user)
        user.save()
        context = {'success':'Successfully Logged In.'}
        return redirect('login')
    
    return render(request,'signup.html')
