# Generated by Django 3.1.2 on 2021-02-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_auto_20210205_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
