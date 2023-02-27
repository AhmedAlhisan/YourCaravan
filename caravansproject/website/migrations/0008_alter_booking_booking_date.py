# Generated by Django 4.1.5 on 2023-02-27 08:29

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_caravan_carvan_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 2, 27, 11, 29, 36, 675856))]),
        ),
    ]