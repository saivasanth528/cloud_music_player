# Generated by Django 2.0.5 on 2018-09-16 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
