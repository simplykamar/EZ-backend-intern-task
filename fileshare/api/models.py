from django.db import models
from django.contrib.auth.models import User
from django.db import models
# from .validators import validate_file_extension

class Profile(models.Model):
    USER_TYPES = [
        ('ops', 'Operation User'),
        ('client', 'Client User')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=6, choices=USER_TYPES)

    def __str__(self):
        return self.user.username

class File(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.uploader.username
