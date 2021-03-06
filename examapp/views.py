from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    return render(request, 'home.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username='username', password='password')
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            if user.is_user:
                return redirect('user_home')
        else:
            messages.info(request, 'invalid credentials')
    return render(request, 'login.html')


