# Generated by Django 3.1.2 on 2020-12-08 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on'], 'verbose_name': 'Blog Post', 'verbose_name_plural': 'Blog Posts'},
        ),
    ]
