# Generated by Django 3.1.4 on 2021-03-21 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0002_remove_question_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='question',
            new_name='QuestionModel',
        ),
    ]
