# Generated by Django 3.1.7 on 2021-03-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0026_auto_20210227_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_type', models.CharField(choices=[('LI', 'Low Intensity'), ('MI', 'Med Intensity'), ('HI', 'High Intensity')], default='MI', max_length=2)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name of App')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, max_length=255, null=True, upload_to='apps/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(db_index=True, default=True)),
            ],
        ),
    ]