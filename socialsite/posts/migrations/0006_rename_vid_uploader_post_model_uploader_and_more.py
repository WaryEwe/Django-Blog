# Generated by Django 5.0.3 on 2024-09-19 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_model',
            old_name='vid_uploader',
            new_name='uploader',
        ),
        migrations.RenameField(
            model_name='post_model',
            old_name='posted_date',
            new_name='video_date',
        ),
        migrations.RenameField(
            model_name='post_model',
            old_name='video',
            new_name='video_file',
        ),
    ]
