# Generated by Django 5.1.3 on 2024-11-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lasoblog', '0003_newblog_blogimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newblog',
            name='blogimage',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]
