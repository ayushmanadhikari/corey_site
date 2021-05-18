from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)              #captures the instance when the image is about to be saved

        img = Image.open(self.image.path)         #opens the image of curent instance

        if img.height>300 or img.width>300:
            output_size = (300,300)             #tuple of max size
            img.thumbnail(output_size)          #resizes image
            img.save(self.image.path)           #saves image to the save path self.image.path
