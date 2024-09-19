from django.forms import ModelForm
from .models import Post_Model

class Post_Form(ModelForm):
    class Meta:
        model = Post_Model
        fields = ['video_file', 'video_title']