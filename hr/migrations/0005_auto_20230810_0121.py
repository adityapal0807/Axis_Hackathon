# Generated by Django 3.2.12 on 2023-08-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_remove_applied_resume_resume_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='visited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='applied_resume',
            name='resume_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
