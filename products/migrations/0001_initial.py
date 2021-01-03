# Generated by Django 3.1.2 on 2021-01-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='products/%Y/%m/%d/')),
                ('affiliate_link', models.CharField(blank=True, max_length=120)),
                ('description_overview', models.CharField(blank=True, max_length=120)),
                ('brand', models.CharField(blank=True, max_length=120)),
                ('dimensions', models.CharField(blank=True, max_length=120)),
                ('model_number', models.CharField(blank=True, max_length=120)),
                ('manufacturer', models.CharField(blank=True, max_length=120)),
                ('colour', models.CharField(blank=True, max_length=120)),
                ('formfactor', models.CharField(blank=True, max_length=120)),
                ('screen_size', models.CharField(blank=True, max_length=120)),
                ('resolution', models.CharField(blank=True, max_length=120)),
                ('processor_brand', models.CharField(blank=True, max_length=120)),
                ('processor_type', models.CharField(blank=True, max_length=120)),
                ('processor_speed', models.CharField(blank=True, max_length=120)),
                ('ram_size', models.CharField(blank=True, max_length=120)),
                ('memory_type', models.CharField(blank=True, max_length=120)),
                ('harddisk_type', models.CharField(blank=True, max_length=120)),
                ('graphics_chipset_brand', models.CharField(blank=True, max_length=120)),
                ('graphics_interface', models.CharField(blank=True, max_length=120)),
                ('graphics_type', models.CharField(blank=True, max_length=120)),
                ('operating_system', models.CharField(blank=True, max_length=120)),
                ('battery_life', models.CharField(blank=True, max_length=120)),
                ('weight', models.CharField(blank=True, max_length=120)),
                ('featured', models.BooleanField(blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
