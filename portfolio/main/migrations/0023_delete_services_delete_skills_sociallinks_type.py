# Generated by Django 4.2.7 on 2023-12-05 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_services_img_alter_skills_img_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='type',
            field=models.CharField(choices=[('socialLinks', 'sochial links'), ('services', 'services'), ('skills', 'skills')], default=1, max_length=11),
            preserve_default=False,
        ),
    ]
