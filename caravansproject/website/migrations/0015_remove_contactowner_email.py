# Generated by Django 4.1.5 on 2023-02-28 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_contactowner_delete_contactus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactowner',
            name='email',
        ),
    ]
