from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.user.models import User, UserProfile


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
