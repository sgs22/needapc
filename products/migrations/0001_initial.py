# Generated by Django 3.1.2 on 2020-10-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('brand', models.CharField(blank=True, max_length=120)),
                ('modelNumber', models.CharField(blank=True, max_length=120)),
                ('size', models.CharField(blank=True, max_length=120)),
                ('weight', models.CharField(blank=True, max_length=120)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
