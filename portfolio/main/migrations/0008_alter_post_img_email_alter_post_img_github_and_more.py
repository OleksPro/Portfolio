# Generated by Django 4.2.7 on 2023-11-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_post_img_email_alter_post_img_github_and_more'),
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
