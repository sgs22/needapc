# Generated by Django 3.1.2 on 2021-01-23 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20210123_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('quiztaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiztakers')),
                ('response_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.choice')),
            ],
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='questions_count',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
