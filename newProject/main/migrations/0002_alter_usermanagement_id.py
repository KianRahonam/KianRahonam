# Generated by Django 4.1.5 on 2023-03-13 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanagement',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]