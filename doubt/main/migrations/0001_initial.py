# Generated by Django 4.1 on 2022-12-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('emailID', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('firstName', models.CharField(default='', max_length=25)),
                ('lastName', models.CharField(default='', max_length=25)),
                ('phoneNumber', models.CharField(default='0000000000', max_length=12)),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
    ]
