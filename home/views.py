from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProfileEditForm

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def view_profile(request):
    return render(request, 'view_profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = str(request.POST.get("username")).lower()
        password = request.POST.get("password")

        filter_dict = {'email': username} if '@' in username and '.' in username else {'username': username}

        user = User.objects.filter(**filter_dict).first()

        if user:
            auth_user = authenticate(request, username=user.username, password=password)
            if auth_user:
                auth_login(request, auth_user)
                return redirect('dashboard') 
            else:
                messages.error(request, 'Invalid username or password')
                print(f"Invalid login attempt: Username, Password")
        else:
            messages.error(request, 'User not found')


    return render(request, 'login.html')


def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('Username') 
        email = request.POST.get('email')
        password = request.POST.get('Password')

     
        if not username or not email or not password:
            return render(request, 'signUp.html', {'error': 'All fields are required'})

      
        if User.objects.filter(username=username).exists():
            return render(request, 'signUp.html', {'error': 'Username already exists'})

        try:
          
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            return redirect('login')
        except IntegrityError:
            return render(request, 'signUp.html', {'error': 'An error occurred while creating the account'})

    return render(request, 'signUp.html')

