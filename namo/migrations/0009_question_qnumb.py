# Generated by Django 3.0.6 on 2020-07-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namo', '0008_profile_qdon'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qnumb',
            field=models.CharField(max_length=15, null=True),
        ),
    ]