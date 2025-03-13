# abcpHome/views.py
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import CombinedForm, UserProfileForm
from .models import TechDot, UserProfile, Prayer, PrayerIntercession, SharedPrayer, SavedPrayer, Post, Comment, PageContent

def generate_random_gradient():
    colors = [
        "#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF", "#33FFF5",
        "#FF8C33", "#33FF8C", "#8C33FF", "#FF338C", "#33A1FF", "#A1FF33"
    ]
    color1 = random.choice(colors)
    color2 = random.choice(colors)
    while color2 == color1:
        color2 = random.choice(colors)
    return f"linear-gradient(to right, {color1}, {color2})"

def home(request):
    gradient = generate_random_gradient()
    return render(request, 'abcpHome/home.html', {'gradient': gradient})

def potb(request):
    gradient = generate_random_gradient()
    tech_dots = TechDot.objects.all()
    content = PageContent.objects.first()  # Assuming you have only one content entry
    return render(request, 'abcpHome/potb.html', {'tech_dots': tech_dots, 'gradient': gradient, 'content': content})

def tech_dot_detail(request, pk):
    gradient = generate_random_gradient()
    tech_dot = get_object_or_404(TechDot, pk=pk)
    return render(request, 'abcpHome/tech_dot_detail.html', {'tech_dot': tech_dot, 'gradient': gradient})

def signup(request):
    gradient = generate_random_gradient()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'abcpHome/signup.html', {'form': form, 'gradient': gradient})

def login_register(request):
    gradient = generate_random_gradient()
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
                try:
                    user = User.objects.create_user(username=register_username, email=register_email, password=register_password1)
                    auth_login(request, user)
                    return redirect('potb')
                except IntegrityError:
                    form.add_error(None, "Username already exists. Please choose a different username.")
    else:
        form = CombinedForm()
    
    return render(request, 'abcpHome/login_register.html', {'form': form, 'gradient': gradient})

def terms_and_conditions(request):
    return render(request, 'abcpHome/termsandconditions.html')

@login_required
def profile(request, username):
    gradient = generate_random_gradient()
    user = get_object_or_404(User, username=username)
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    my_prayers = Prayer.objects.filter(user=user)
    prayer_intercessions = PrayerIntercession.objects.filter(user=user)
    shared_prayers = SharedPrayer.objects.filter(user=user)
    saved_prayers = SavedPrayer.objects.filter(user=user)

    context = {
        'profile_user': user,
        'user_profile': user_profile,
        'my_prayers': my_prayers,
        'prayer_intercessions': prayer_intercessions,
        'shared_prayers': shared_prayers,
        'saved_prayers': saved_prayers,
        'gradient': gradient,
    }
    return render(request, 'abcpHome/profile.html', context)

@login_required
def edit_profile(request):
    gradient = generate_random_gradient()
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'abcpHome/edit_profile.html', {'form': form, 'gradient': gradient})

def news_feed(request):
    gradient = generate_random_gradient()
    my_prayers = Post.objects.filter(category='my_prayers').order_by('-created_at')
    prayer_intercessions = Post.objects.filter(category='prayer_intercessions').order_by('-created_at')
    context = {
        'my_prayers': my_prayers,
        'prayer_intercessions': prayer_intercessions,
        'gradient': gradient,
    }
    return render(request, 'abcpHome/news_feed.html', context)

@login_required
def add_my_prayer(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        # Assuming you have a Post model with category 'my_prayers' and a user is logged in
        Post.objects.create(user=request.user, content=content, category='my_prayers')
        return redirect('news_feed')
    return HttpResponse(status=405)  # Method Not Allowed

@login_required
def add_prayer_intercession(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        # Assuming you have a Post model with category 'prayer_intercessions' and a user is logged in
        Post.objects.create(user=request.user, content=content, category='prayer_intercessions')
        return redirect('news_feed')
    return HttpResponse(status=405)  # Method Not Allowed
