from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('users', self.username, instance)
        return None

    avatar = models.ImageField(upload_to=image_upload_to, default='images/1234.jpg', blank=True, null=True)
    bio = models.TextField(max_length=410, blank=True, null=True)
    instagram = models.URLField(blank=True, null=True, verbose_name='instagram:')
    phone = models.CharField(blank=True, max_length=20, verbose_name='User phone')
    slug = models.SlugField(max_length=300, unique=True, db_index=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'user'

    def save(self, *args, **kwargs):  # save slug new user
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
