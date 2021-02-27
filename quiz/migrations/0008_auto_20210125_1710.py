# Generated by Django 3.1.2 on 2021-01-25 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20210123_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id'], 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.RenameField(
            model_name='question',
            old_name='description_text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='selected',
        ),
        migrations.RemoveField(
            model_name='question',
            name='created',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='questions_count',
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.IntegerField(choices=[(1, 'One answer'), (2, 'Multiple answer'), (3, 'Text answer')], default=1, verbose_name='Question Type'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question', verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Is active?'),
        ),
    ]