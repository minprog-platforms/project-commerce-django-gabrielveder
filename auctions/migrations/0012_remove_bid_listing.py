# Generated by Django 4.1.3 on 2022-12-16 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_listing_current_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='listing',
        ),
    ]