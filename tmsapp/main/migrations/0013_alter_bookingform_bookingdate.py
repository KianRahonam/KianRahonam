# Generated by Django 4.1.1 on 2022-10-08 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_bookingform_loadtype_alter_bookingform_bookingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingform',
            name='bookingDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 8, 12, 16, 57, 434375)),
        ),
    ]