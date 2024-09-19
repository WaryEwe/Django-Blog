from django.db import models
from django.contrib.auth.models import User

class Post_Model(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    video_title =models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    video_date = models.DateField(auto_now_add=True)