# Generated by Django 3.1.2 on 2020-10-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiceApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'Vendor'), (2, 'Bidder')], default=None),
        ),
    ]