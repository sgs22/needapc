# Generated by Django 3.1.2 on 2021-02-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20210127_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='response_option',
        ),
        migrations.AddField(
            model_name='userresponse',
            name='response_1',
            field=models.CharField(blank=True, default=True, max_length=255),
        ),
    ]