# Generated by Django 3.1.2 on 2021-01-27 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20210125_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiztakers',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='quiztakers',
            name='selected_answers',
        ),
    ]
