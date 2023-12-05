# Generated by Django 4.2.7 on 2023-12-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_delete_services_delete_skills_sociallinks_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallinks',
            name='type',
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='category',
            field=models.CharField(choices=[('socialLinks', 'Sochial links'), ('services', 'Services'), ('skills', 'Skills')], default=1, max_length=11),
            preserve_default=False,
        ),
    ]
