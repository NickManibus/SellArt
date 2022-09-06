from django.db import models
from user.models import User
from embed_video.fields import EmbedVideoField
from django.dispatch.dispatcher import receiver
from PIL import Image
from django.urls import reverse
from django.utils.text import slugify
from django_resized import ResizedImageField
from pytils.translit import slugify


class FeedBackContact(models.Model):
    full_name = models.CharField(max_length=250, verbose_name='First Name, Last Name:')
    email = models.EmailField(verbose_name='Email: ')
    message = models.TextField(verbose_name='message:')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created:')
    active = models.BooleanField(default=True, verbose_name='in work')

    class Meta:
        db_table = 'Contact_massages'
        unique_together = ('full_name', 'email', 'active')
        verbose_name = 'New message'
        verbose_name_plural = 'New messages'


class Video(models.Model):
    title = models.CharField(max_length=250)
    name = models.CharField("Name", max_length=100)
    file = models.FileField(upload_to='works/video/%Y/%m/%d/%H/%M%S', blank=True, null=True)
    description = models.TextField("Description", max_length=1010)
    email = models.EmailField(blank=True, verbose_name='Email: ')
    social = models.URLField(blank=True)
    slug = models.SlugField(blank=True, unique=True, db_index=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time of creation")
    video_url = EmbedVideoField()

    class Meta:
        db_table = 'Video'

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('single_video', kwargs={'slug': self.slug})


class Work(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    image = ResizedImageField(size=[1920, 1350], force_format='jpeg', crop=['middle', 'center'],
                              upload_to='works/%Y/%m/%d/', )
    image1 = ResizedImageField(size=[1920, 1350], force_format='jpeg', crop=['middle', 'center'],
                               upload_to='works/%Y/%m/%d/', )
    image2 = ResizedImageField(size=[1920, 1350], force_format='jpeg', crop=['middle', 'center'],
                               upload_to='works/%Y/%m/%d/', )
    email = models.EmailField(blank=True, verbose_name='Email: ')
    full_name = models.CharField(max_length=250, verbose_name='First Name, Last Name:', blank=True)
    text = models.TextField(max_length=1000)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    slug = models.SlugField(blank=True, null=True, db_index=True)  # TODO: autoset
    instagram = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField('Tags', blank=True, related_name='work_tag')
    is_moderated = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time of creation")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Change time")

    class Meta:
        db_table = 'Works'
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('users_profile', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tags(models.Model):
    # TODO: validators for name
    name = models.CharField(max_length=35, verbose_name='#tag')
    slug = models.SlugField(max_length=30, blank=True)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    class Meta:
        db_table = 'Tags_work'
        verbose_name = 'Tag'

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='works/%Y/%m/%d/', )
    new_post = models.ForeignKey(Work, verbose_name='work_image', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.image)
