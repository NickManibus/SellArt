import pathlib
from datetime import datetime
from django.db import models
from django.dispatch.dispatcher import receiver
from user.models import User
from random import randrange
from django.urls import reverse


class Post(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )

    author = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/%Y/%m/%d/%H/%M%S', null=True, blank=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    is_updated = models.BooleanField(default=False)
    is_moderated = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(blank=True, unique=True, db_index=True)  # TODO: autoset
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time of creation")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Change time")
    tags = models.ManyToManyField('Tags', blank=True, related_name='posts')

    class Meta:
        db_table = 'post'
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_success_url(self):
        return reverse('post', kwargs={'post_slug': self.slug.object.id})


class Comment(models.Model):

    def file_path(self, filename):
        file = pathlib.Path(filename)
        ext = file.suffix or '.png'
        path = (datetime.strftime(datetime.now(), 'post/comment/%Y/%m/%d/%H/%M%S')
                + str(round(datetime.now().timestamp() * 1000000))
                + str(randrange(1, 1000000))
                )
        return path + ext

    text = models.TextField(verbose_name='Message')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    is_moderated = models.BooleanField(default=False)
    image = models.ImageField(upload_to=file_path, null=True, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    is_updated = models.BooleanField(default=False)
    email = models.EmailField()

    class Meta:
        db_table = 'comments'
        ordering = ('created',)

    def __str__(self):
        return f'Comment for {self.post.title}: {self.id}'


class Tags(models.Model):
    name = models.CharField(max_length=35, verbose_name='#tag')
    slug = models.SlugField(max_length=30, blank=True)

    def get_absolute_url(self):
        return reverse('post/detail_tag.html', kwargs={'slug': self.slug})

    class Meta:
        db_table = 'Tags_post'
        verbose_name = 'Tag'

    def __str__(self):
        return self.name


@receiver(models.signals.pre_save, sender=Tags)
def edit_tag(sender, instance, **kwargs):
    if not instance.name.startswith('#'):
        instance.name = '#' + instance.name
        instance.slug = instance.name.strip('#')
