# Generated by Django 4.2.3 on 2023-07-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_trail_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='map',
            field=models.TextField(default='https://maps/google.com'),
        ),
    ]