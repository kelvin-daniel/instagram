# Generated by Django 3.1.2 on 2020-10-24 07:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0002_profile_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]