# Generated by Django 4.2.7 on 2024-01-17 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allimages',
            name='text',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='allimages',
            name='text_uk',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
