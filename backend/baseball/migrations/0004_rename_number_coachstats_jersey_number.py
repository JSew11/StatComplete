# Generated by Django 4.1.6 on 2023-02-14 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0003_alter_coachstats_stats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coachstats',
            old_name='number',
            new_name='jersey_number',
        ),
    ]
