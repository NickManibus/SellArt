# Generated by Django 4.0.4 on 2022-09-06 17:02

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_work_image_alter_work_image1_alter_work_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='works/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='jpeg', keep_meta=True, quality=75, scale=0.5, size=[1200, 1080], upload_to='works/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='work',
            name='image1',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='jpeg', keep_meta=True, quality=75, scale=0.5, size=[1200, 1080], upload_to='works/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='work',
            name='image2',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='jpeg', keep_meta=True, quality=75, scale=0.5, size=[1200, 1080], upload_to='works/%Y/%m/%d/'),
        ),
    ]
