# Generated by Django 4.1.5 on 2023-02-22 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_booking_is_payed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Note',
            new_name='note',
        ),
    ]