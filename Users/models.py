from django.db import models
from django.contrib.auth.models import User
from NGO.models import ngos

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'images/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
class Volunteer(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    ngos_volunteering = models.ManyToManyField(ngos, related_name='volunteers')

    def __str__(self):
        return f'{self.user_profile.user.username} volunteering'