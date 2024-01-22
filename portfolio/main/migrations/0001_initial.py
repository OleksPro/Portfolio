# Generated by Django 4.2.7 on 2024-01-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(blank=True, null=True)),
                ('text_uk', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, upload_to='all_images')),
                ('category', models.CharField(blank=True, choices=[('services', 'Services'), ('skills', 'Skills'), ('learning', 'learning')], max_length=11)),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'All images',
            },
        ),
        migrations.CreateModel(
            name='AllLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='site_images')),
                ('link', models.URLField(blank=True, null=True)),
                ('category', models.CharField(blank=True, choices=[('social_links', 'social_links'), ('site_links', 'site_links'), ('footer_links', 'footer_links')], max_length=12)),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'All links',
            },
        ),
    ]