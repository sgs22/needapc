# Generated by Django 3.1.2 on 2020-10-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_productdetail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='image',
            field=models.ImageField(blank=True, max_length=200, upload_to='products'),
        ),
    ]
