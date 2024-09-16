from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(blank=True)
    
    is_creator = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username



