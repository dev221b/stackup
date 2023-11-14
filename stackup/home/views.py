from django.shortcuts import render, redirect, HttpResponse 
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'index.html')

def landingPage(request):
    return render(request, 'landingpage.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.first_name
            return render(request, 'landingpage.html', {'name': name})
        
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('login')
        
    return render(request, 'login.html')

def signupp(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        password = request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('signup')
        
        
        if len(username)>10:
            messages.error(request, "Username less than 10 characters please")
            return redirect('signup')


        if not username.isalnum():
            messages.error(request, "Username should be Alpha Numeric")
            return redirect('signup')
        
        myuser = User.objects.create_user(username,' ',password)
        myuser.first_name = name
        myuser.save()
        
        messages.success(request, "Your account created successfully")

        return redirect('login')

    return render(request, 'signup.html')


def loggout(request):
    logout(request)
    messages.success(request, 'logout sucess')
    return redirect('index')