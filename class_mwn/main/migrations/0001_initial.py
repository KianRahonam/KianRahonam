# Generated by Django 4.1.5 on 2023-03-11 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserManagement',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
