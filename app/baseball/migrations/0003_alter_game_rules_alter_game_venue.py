# Generated by Django 4.2 on 2023-05-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0002_alter_game_rules_alter_game_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rules',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='venue',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
