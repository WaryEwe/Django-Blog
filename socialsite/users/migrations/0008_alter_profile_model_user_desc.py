# Generated by Django 5.0.3 on 2024-09-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_model_user_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_model',
            name='user_desc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
