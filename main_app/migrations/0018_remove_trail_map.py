# Generated by Django 4.2.3 on 2023-07-17 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_remove_trail_images_trail_image_alter_trail_map_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='map',
        ),
    ]
