# Generated by Django 4.2.7 on 2023-12-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_alter_alllinks_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allimages',
            name='category',
            field=models.CharField(blank=True, choices=[('services', 'Services'), ('skills', 'Skills'), ('learning', 'learning')], max_length=11),
        ),
        migrations.AlterField(
            model_name='alllinks',
            name='category',
            field=models.CharField(blank=True, choices=[('social_links', 'social_links'), ('site_links', 'site_links'), ('footer_links', 'footer_links')], max_length=12),
        ),
    ]
