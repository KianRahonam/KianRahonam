# Generated by Django 4.1.1 on 2022-10-08 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_bookingform_mot_alter_bookingform_bookingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchoffice',
            name='lrnumberSl',
            field=models.CharField(default=20220000, max_length=8),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='bookingDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 8, 19, 40, 42, 784874)),
        ),
    ]
