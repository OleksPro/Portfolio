# Generated by Django 4.2.7 on 2023-12-05 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_sociallinks_type_sociallinks_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialLinks',
            new_name='AllImages',
        ),
        migrations.AlterModelOptions(
            name='allimages',
            options={'verbose_name': 'image', 'verbose_name_plural': 'All images'},
        ),
    ]
