# Generated by Django 4.1.5 on 2023-01-17 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=9)),
                ('bus_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_id', models.AutoField(primary_key=True, serialize=False)),
                ('seat_number', models.IntegerField()),
                ('seat_status', models.BooleanField()),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketSystem.bus')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_status', models.BooleanField()),
                ('ticket_price', models.IntegerField()),
                ('ticket_date', models.DateField()),
                ('ticket_time', models.TimeField()),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketSystem.bus')),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketSystem.seat')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketSystem.user')),
            ],
        ),
    ]