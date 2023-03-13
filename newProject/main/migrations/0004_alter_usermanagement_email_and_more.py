# Generated by Django 4.1.5 on 2023-03-13 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_usermanagement_ps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanagement',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usermanagement',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usermanagement',
            name='gender',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='usermanagement',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usermanagement',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='usermanagement',
            name='role',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
