# Generated by Django 3.1.7 on 2021-03-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_productimage_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='products/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='products/images/%Y/%m/%d/'),
        ),
    ]
