# Generated by Django 4.1.5 on 2023-01-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('sal', models.DecimalField(decimal_places=4, max_digits=12)),
            ],
        ),
    ]