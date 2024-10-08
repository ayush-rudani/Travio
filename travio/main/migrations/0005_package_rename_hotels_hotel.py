# Generated by Django 4.0.1 on 2022-03-29 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('tourId', models.IntegerField(primary_key=True, serialize=False)),
                ('packageTitle', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('adeventure', 'Adeventure'), ('wildlife', 'Wildlife'), ('pilgrimage', 'Pilgrimage'), ('family', 'Family'), ('honeymoon', 'Honeymoon')], default='adeventure', max_length=32)),
                ('image', models.CharField(max_length=50)),
                ('packageDesc', models.TextField()),
                ('duration', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('disPrice', models.IntegerField()),
                ('discount', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Hotels',
            new_name='Hotel',
        ),
    ]
