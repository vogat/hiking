# Generated by Django 4.2.3 on 2023-07-17 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_trail_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=[4], max_length=1)),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.trail')),
            ],
        ),
    ]
