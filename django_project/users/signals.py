from django.db.models.signals import post_save      #signal that gets fired after an object is saved
from django.contrib.auth.models import User         #signal sender
from django.dispatch import receiver                #signal reciever - a function that gets signal and performs some task
from .models import Profile                         #we will be creating profile in our function


#this just creates profile everytime a user gets created
@receiver(post_save, sender=User)                    
def create_profile(sender, instance, created, **kwargs):        #these arguments are sent by post_save signal
    if created:
        Profile.objects.create(user=instance)                   #the profile object gets created

#this saves the profile everytime the user gets saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
