# Generated by Django 3.0.6 on 2020-07-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namo', '0002_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='que',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
