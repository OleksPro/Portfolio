# Generated by Django 4.2.7 on 2023-12-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_rename_link_portfoliosites_site_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliosites',
            name='img',
            field=models.ImageField(blank=True, upload_to='site_images'),
        ),
    ]