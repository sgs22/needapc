# Generated by Django 3.1.7 on 2021-03-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('featured', '0002_auto_20201130_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredpost',
            name='content',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
