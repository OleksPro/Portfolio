# Generated by Django 4.2.7 on 2023-11-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_post_img_it'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_separator',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
