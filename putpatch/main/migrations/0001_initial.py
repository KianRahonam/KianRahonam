# Generated by Django 4.1 on 2022-12-24 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IssueTickets',
            fields=[
                ('ticketNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('createdBy', models.CharField(default='', max_length=25)),
                ('issueDetial', models.CharField(default='', max_length=150)),
                ('status', models.CharField(default='', max_length=20)),
                ('assignedTo', models.CharField(default='admin', max_length=25)),
            ],
        ),
    ]
