# Generated by Django 4.0.1 on 2022-03-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('hotelId', models.IntegerField(primary_key=True, serialize=False)),
                ('hotelName', models.CharField(max_length=100)),
                ('hotelAddress', models.TextField()),
                ('pinCode', models.IntegerField()),
                ('hotelDesc', models.TextField()),
                ('roomType', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available', max_length=32)),
            ],
        ),
    ]