# Generated by Django 3.1.2 on 2021-02-10 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0022_auto_20210210_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.question'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='quiz.quiz'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]