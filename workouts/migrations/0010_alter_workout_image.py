# Generated by Django 3.2.4 on 2021-07-12 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0009_workout_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='workout_pics'),
        ),
    ]
