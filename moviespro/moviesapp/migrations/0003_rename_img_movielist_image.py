# Generated by Django 3.2.14 on 2022-08-12 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0002_movielist_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movielist',
            old_name='img',
            new_name='image',
        ),
    ]