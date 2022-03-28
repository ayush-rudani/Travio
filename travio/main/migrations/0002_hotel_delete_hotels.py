# Generated by Django 4.0.1 on 2022-03-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotelId', models.IntegerField(primary_key=True, serialize=False)),
                ('hotelName', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('hotelAddress', models.TextField()),
                ('pinCode', models.IntegerField()),
                ('hotelDesc', models.TextField()),
                ('roomType', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available', max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='Hotels',
        ),
    ]
