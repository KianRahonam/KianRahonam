# Generated by Django 4.1.1 on 2022-10-10 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_branchoffice_lrnumbersl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingform',
            name='billingAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='billingType',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='bookingBranch',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='bookingDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 10, 15, 14, 38, 560744), null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='consignee',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='consignore',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='deliveryAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='deliveryBranch',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='deliveryType',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='docDate',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='docNumber',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='fgstn',
            field=models.CharField(default=29000000000, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='freightAmount',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='hamaliCharges',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='invWeight',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='loadType',
            field=models.CharField(default='FTL', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='lrNumber',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='mot',
            field=models.CharField(default='Road', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='ngstn',
            field=models.CharField(default=29000000000, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='noa',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='packType',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='remark',
            field=models.CharField(default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='status',
            field=models.CharField(default='Ready', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='value',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='vehicleNumber',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='weight',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='branchoffice',
            name='branchAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='branchoffice',
            name='branchCity',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='branchoffice',
            name='branchName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='branchoffice',
            name='branchState',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='branchoffice',
            name='contactNumber',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='branchoffice',
            name='emailId',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='branchoffice',
            name='lrnumberSl',
            field=models.CharField(default=20220000, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='branchoffice',
            name='ownerShip',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='branchoffice',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
