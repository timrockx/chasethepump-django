# Generated by Django 3.2.4 on 2021-07-22 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0011_auto_20210722_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='equipment',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='workout',
            name='sets',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='workout',
            name='video',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
