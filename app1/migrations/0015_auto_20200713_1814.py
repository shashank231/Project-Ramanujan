# Generated by Django 3.0.6 on 2020-07-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_profile_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
