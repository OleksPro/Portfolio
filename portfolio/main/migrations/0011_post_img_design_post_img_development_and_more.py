# Generated by Django 4.2.7 on 2023-11-27 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_post_img_separator'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_design',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_development',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_maintenance',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
