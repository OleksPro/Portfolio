# Generated by Django 4.2.7 on 2023-11-28 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_sociallinks_alt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_main',
        ),
    ]
