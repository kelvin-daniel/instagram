# Generated by Django 3.1.2 on 2020-10-24 07:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20201017_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
