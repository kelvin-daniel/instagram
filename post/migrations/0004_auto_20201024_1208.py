# Generated by Django 3.1.2 on 2020-10-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20201024_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to='images/', verbose_name='Picture'),
        ),
    ]
