# Generated by Django 4.2.3 on 2023-07-17 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_alter_rating_difficulty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='score',
            new_name='trail',
        ),
    ]
