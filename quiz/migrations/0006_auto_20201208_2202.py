# Generated by Django 3.1.2 on 2020-12-08 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_question_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='image',
            new_name='question_image',
        ),
    ]
