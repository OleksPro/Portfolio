# Generated by Django 4.2.7 on 2023-11-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_post_img_email_alter_post_img_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_it',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
