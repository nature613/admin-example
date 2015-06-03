from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """
    An extension of the django user.
    """
    email_notifications = models.BooleanField("Allows email notifications", default=True)
    avatar = models.ImageField("Avatar", upload_to="avatars", blank=True, null=True)
