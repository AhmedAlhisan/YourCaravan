# Generated by Django 4.1.5 on 2023-02-22 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_booking_is_payed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='appointmentUser',
            new_name='bookinUser',
        ),
    ]
