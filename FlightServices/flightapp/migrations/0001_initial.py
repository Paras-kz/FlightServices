# Generated by Django 4.1.5 on 2023-03-05 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightNumber', models.CharField(max_length=10)),
                ('operatingAirlines', models.CharField(max_length=20)),
                ('departureCity', models.CharField(max_length=20)),
                ('arrivalCity', models.CharField(max_length=20)),
                ('dateOfDeparture', models.DateField()),
                ('estimatedTimeOfDeparture', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('middleName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightapp.flight')),
                ('passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightapp.passenger')),
            ],
        ),
    ]
