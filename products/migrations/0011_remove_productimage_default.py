# Generated by Django 3.1.7 on 2021-03-19 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210319_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='default',
        ),
    ]