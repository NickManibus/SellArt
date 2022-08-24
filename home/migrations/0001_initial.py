# Generated by Django 4.0.4 on 2022-08-21 01:18

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBackContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, verbose_name='First Name, Last Name:')),
                ('email', models.EmailField(max_length=254, verbose_name='Email: ')),
                ('message', models.TextField(verbose_name='message:')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created:')),
                ('active', models.BooleanField(default=True, verbose_name='in work')),
            ],
            options={
                'verbose_name': 'New message',
                'verbose_name_plural': 'New messages',
                'db_table': 'Contact_massages',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='works/%Y/%m/%d/%H/%M%S')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='#tag')),
                ('slug', models.SlugField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name': 'Tag',
                'db_table': 'Tags_work',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('file', models.FileField(blank=True, null=True, upload_to='works/video/%Y/%m/%d/%H/%M%S')),
                ('description', models.TextField(max_length=1010, verbose_name='Description')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email: ')),
                ('social', models.URLField(blank=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')),
                ('video_url', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'db_table': 'Video',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='works/%Y/%m/%d/%H/%M%S')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='works/%Y/%m/%d/%H/%M%S')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='works/%Y/%m/%d/%H/%M%S')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email: ')),
                ('full_name', models.CharField(blank=True, max_length=250, verbose_name='First Name, Last Name:')),
                ('text', models.TextField(max_length=1000)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('social', models.URLField(blank=True, null=True)),
                ('is_moderated', models.BooleanField(default=False)),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Change time')),
            ],
            options={
                'db_table': 'Works',
                'ordering': ['-id'],
            },
        ),
    ]