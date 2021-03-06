# Generated by Django 2.2.1 on 2020-11-23 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def question_type_forward(apps, schema_editor):
    QuestionType = apps.get_model("polls", "QuestionType")
    db_alias = schema_editor.connection.alias
    QuestionType.objects.using(db_alias).bulk_create([
        QuestionType(name="Текстовый ответ"),
        QuestionType(name="Ответ с одним вариантом"),
        QuestionType(name="Ответ с несколькими вариантами"),
    ])


def question_type_reverse(apps, schema_editor):
    QuestionType = apps.get_model("polls", "QuestionType")
    db_alias = schema_editor.connection.alias
    QuestionType.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Вариант')),
            ],
            options={
                'verbose_name': 'Вариант ответа на вопрос',
                'verbose_name_plural': 'Варианты ответов на вопросы',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название опроса')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_start', models.DateTimeField(verbose_name='Дата старта')),
                ('date_end', models.DateTimeField(verbose_name='Дата окончания')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Текст вопроса')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.Poll', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Тип опроса',
                'verbose_name_plural': 'Типы опросов',
            },
        ),
        migrations.CreateModel(
            name='UserChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текстовый вариант ответа')),
                ('answers', models.ManyToManyField(blank=True, to='polls.AnswerOption', verbose_name='Варианты ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_choices', to='polls.Question', verbose_name='Вопрос')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Вариант ответа пользователя',
                'verbose_name_plural': 'Варианты ответов пользователей',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.QuestionType', verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='answeroption',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.Question', verbose_name='Вопрос'),
        ),
        migrations.RunPython(question_type_forward, question_type_reverse)

    ]
