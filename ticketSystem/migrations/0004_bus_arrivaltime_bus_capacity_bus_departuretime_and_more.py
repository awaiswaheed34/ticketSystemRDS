# Generated by Django 4.1.5 on 2023-02-18 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSystem', '0003_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='arrivalTime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='capacity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='departureTime',
            field=models.TimeField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
