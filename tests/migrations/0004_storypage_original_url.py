# Generated by Django 2.2.17 on 2020-12-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_storypage_image_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='storypage',
            name='original_url',
            field=models.URLField(blank=True, max_length=2047, verbose_name='Original URL'),
        ),
    ]