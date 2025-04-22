
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from .models import LoginInfo
from .models import RegisterInfo
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password

from django.contrib.auth.hashers import check_password 

def home(request):
    return render(request, 'home.html')

# def details(request):
#     student_name = 

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = RegisterInfo.objects.get(username=username)
                if check_password(password,user.password):
                    return redirect('login_completed')

                else :
                    form.add_error("password","Invalid password")

            except LoginInfo.DoesNotExist:
                form.add_error('username',"username not Found")
    return render(request, 'login.html', {'form': form})

def login_completed(request):
    return render(request, 'login_complete.html')  # ✅ Fix this line

def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data =form.cleaned_data

            if RegisterInfo.objects.filter(username=data['username']).exists():
                form.add_error('username', 'username already exists')

            if data['password'] != data['confirm_password']:
                form.add_error('confirm_password', 'Passwords do not match')

            else:
                hashed_password = make_password(data['password'])
                RegisterInfo.objects.create(
                    name =data['name'],
                    email = data['email'],
                    username=data['username'],
                    password= hashed_password,
                    # confirm_password=data['confirm_password'],
                )
            return redirect('register_complete')
    return render(request, 'register.html', {'form': form})

def register_complete(request):  # ✅ Add this view
    return render(request, 'register_complete.html')



def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')
