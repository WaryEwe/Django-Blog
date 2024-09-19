from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile_Model, Post_Model
class Signup_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class Login_Form(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class P_Edit_Form(forms.ModelForm):
    class Meta:
        model = Profile_Model
        fields = ['user_desc']

class Post_Form(forms.ModelForm):
    class Meta:
        model = Post_Model
        fields = ['video', 'video_title']