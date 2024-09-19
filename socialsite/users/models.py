from django.db import models
from django.contrib.auth.models import User

class Profile_Model(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_desc = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.user_id.username
    