# Generated by Django 4.1.1 on 2022-10-04 18:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_bookingform_bookingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingform',
            name='bookingDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 23, 38, 34, 348259)),
        ),
    ]
