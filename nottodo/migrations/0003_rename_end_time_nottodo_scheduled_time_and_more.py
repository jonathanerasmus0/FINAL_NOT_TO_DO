# Generated by Django 5.0.6 on 2024-06-30 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nottodo', '0002_rename_scheduled_time_nottodo_end_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nottodo',
            old_name='end_time',
            new_name='scheduled_time',
        ),
        migrations.RemoveField(
            model_name='nottodo',
            name='start_time',
        ),
    ]