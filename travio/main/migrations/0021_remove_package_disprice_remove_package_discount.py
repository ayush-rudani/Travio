# Generated by Django 4.0.1 on 2022-04-07 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_package_disprice_alter_package_discount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='disPrice',
        ),
        migrations.RemoveField(
            model_name='package',
            name='discount',
        ),
    ]
