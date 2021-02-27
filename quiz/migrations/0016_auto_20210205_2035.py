# Generated by Django 3.1.2 on 2021-02-05 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0015_auto_20210205_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='quiztaker',
        ),
        migrations.AddField(
            model_name='userresponse',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiztaker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='QuizTakers',
        ),
    ]