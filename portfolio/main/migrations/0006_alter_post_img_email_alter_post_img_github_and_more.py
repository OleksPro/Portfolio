# Generated by Django 4.2.7 on 2023-11-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post_img_email_post_img_github_post_img_linkedin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_email',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img_github',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img_linkedin',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img_main',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]