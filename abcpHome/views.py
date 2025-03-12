# abcpHome/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from .forms import CombinedForm
from .models import TechDot

def home(request):
    return render(request, 'abcpHome/home.html')# abcpHome/views.py

from django.shortcuts import render, get_object_or_404
from .models import TechDot

def potb(request):
    tech_dots = TechDot.objects.all()
    return render(request, 'abcpHome/potb.html', {'tech_dots': tech_dots})

def tech_dot_detail(request, pk):
    tech_dot = get_object_or_404(TechDot, pk=pk)
    return render(request, 'abcpHome/tech_dot_detail.html', {'tech_dot': tech_dot})


def login_register(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        if form.is_valid():
            login_username = form.cleaned_data.get('login_username')
            login_password = form.cleaned_data.get('login_password')
            register_email = form.cleaned_data.get('register_email')
            register_username = form.cleaned_data.get('register_username')
            register_password1 = form.cleaned_data.get('register_password1')

            if login_username and login_password:
                # Try to authenticate the user
                user = authenticate(request, username=login_username, password=login_password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('potb')
                else:
                    form.add_error(None, "Invalid login credentials")
            elif register_email and register_password1:
                # Create a new user
                if not register_username:
                    register_username = f"anon_{User.objects.count() + 1}"
                user = User.objects.create_user(username=register_username, email=register_email, password=register_password1)
                auth_login(request, user)
                return redirect('potb')
    else:
        form = CombinedForm()
    
    return render(request, 'abcpHome/login_register.html', {'form': form})

def potb(request):
    tech_dots = TechDot.objects.all()
    return render(request, 'abcpHome/potb.html', {'tech_dots': tech_dots})

def tech_dot_detail(request, pk):
    tech_dot = get_object_or_404(TechDot, pk=pk)
    return render(request, 'abcpHome/tech_dot_detail.html', {'tech_dot': tech_dot})








