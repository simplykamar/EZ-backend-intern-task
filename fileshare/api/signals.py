from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
# @receiver(pre_save, sender=User)
# def pre_save_user(sender, instance, **kwargs):
#     print(f'Pre-save signal: {instance} is about to be saved.')

@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        print(f'Post-save signal: {instance} was created.')
        Profile.objects.create(user=instance,user_type="client")