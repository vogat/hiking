# Generated by Django 4.2.3 on 2023-07-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_trail_city_trail_state_trail_streetaddress_trail_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='map',
            field=models.CharField(default='https://maps/google.com'),
            preserve_default=False,
        ),
    ]
