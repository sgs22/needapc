# Generated by Django 3.1.2 on 2020-10-19 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201019_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetail',
            name='image',
        ),
    ]