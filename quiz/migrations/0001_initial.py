# Generated by Django 5.1.7 on 2025-03-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('topic', models.CharField(choices=[('AI', 'Ai'), ('Cyber Security', 'Cyber Security'), ('Backend', 'Backend'), ('Mobile', 'Mobile')], max_length=50)),
                ('correct_answer_index', models.IntegerField(choices=[(0, 'Option 1'), (1, 'Option 2'), (2, 'Option 3'), (3, 'Option 4')])),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
    ]
