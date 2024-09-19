from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from .forms import Signup_Form, Login_Form, P_Edit_Form, Post_Form
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile_Model, Post_Model

def login_view(request):
    if request.method == 'POST':
        login_f = Login_Form(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user', username=username)
        else:
            messages.error(request, 'Something went wrong!')
    else:
        login_f = Login_Form()
    context = {
        'login_f':login_f,
    }
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        signup_f = Signup_Form(request.POST)
        if signup_f.is_valid():
            signup_f.save()
            return redirect('login')
    else:
        signup_f = Signup_Form()
    context = {
        'signup_f':signup_f,
    }
    return render(request, 'signup.html', context)

def profile_view(request, username):
    req_user = get_object_or_404(User, username=username)
    user_profile, created = Profile_Model.objects.get_or_create(user_id=req_user)
    url_user = reverse('user', kwargs={'username':username})
    user_config = get_object_or_404(Profile_Model, user_id=req_user)
    video_up = Post_Model.objects.filter(vid_uploader=req_user)
    if request.method == 'POST':
        user_desc_f = P_Edit_Form(request.POST, instance=user_profile)
        video_f = Post_Form(request.POST, request.FILES)
        if video_f.is_valid():
            video_u = video_f.save(commit=False)
            video_u.vid_uploader = req_user
            video_u.save()
            return redirect('user', username=username)
        else:
            messages.error(request, 'there was a error!')

        if user_desc_f.is_valid():
            user_desc = user_desc_f.save(commit=False,)
            user_desc.user_id = req_user
            user_desc.save()
            return redirect('user', username=username)
        else:
            messages.error(request, 'test')
            return redirect('test')
    else:
        user_desc_f = P_Edit_Form()
        video_f = Post_Form(instance=request.user)
    
    context = {
        'url_user':url_user,
        'req_user':req_user,
        'username':username,
        'user_desc_f':user_desc_f,
        'user_conifg':user_config,
        'video_f':video_f,
        'video_up':video_up,
    }
    return render(request, 'profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')
