# Generated by Django 4.2.7 on 2023-11-23 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_post_author_remove_post_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='img',
        ),
    ]
