# Generated by Django 3.2.12 on 2023-08-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_hr',
            field=models.BooleanField(default=True),
        ),
    ]
