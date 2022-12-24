# Generated by Django 4.0.5 on 2022-12-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='password',
            field=models.CharField(default='Admin', max_length=100),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='emailId',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='firstname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='lastname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='phoneNum',
            field=models.CharField(default='', max_length=12),
        ),
    ]