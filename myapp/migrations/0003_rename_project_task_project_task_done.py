# Generated by Django 5.0.6 on 2024-06-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Project',
            new_name='project',
        ),
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]