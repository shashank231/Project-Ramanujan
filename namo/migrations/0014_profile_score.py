# Generated by Django 3.0.6 on 2020-07-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namo', '0013_auto_20200713_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
