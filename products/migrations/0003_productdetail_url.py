# Generated by Django 3.1.2 on 2021-01-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_productdetail_affiliate_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='url',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
