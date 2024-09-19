from django.db import models
from django.contrib.auth.models import User

class Profile_Model(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_desc = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.user_id.username
    
class Post_Model(models.Model):
    vid_uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    posted_date = models.DateField(auto_now_add=True)