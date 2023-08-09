# Generated by Django 3.2.12 on 2023-08-09 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_user_is_hr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TEST_CREDENTIALS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_id', to=settings.AUTH_USER_MODEL)),
                ('resume_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_resume', to='hr.applied_resume')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Chat_History',
        ),
    ]
