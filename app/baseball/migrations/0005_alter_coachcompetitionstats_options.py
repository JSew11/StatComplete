# Generated by Django 4.1.7 on 2023-03-03 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0004_remove_team_record_competitionteam_record'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coachcompetitionstats',
            options={'ordering': ['created'], 'verbose_name': 'Coach Stats (Competition)', 'verbose_name_plural': 'Coach Stats (Competition)'},
        ),
    ]
