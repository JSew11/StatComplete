# Generated by Django 4.2 on 2023-05-12 16:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamplayer',
            name='batting_totals',
        ),
        migrations.RemoveField(
            model_name='teamplayer',
            name='fielding_totals',
        ),
        migrations.CreateModel(
            name='PlayerGameStats',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('batting', models.JSONField(default=dict)),
                ('fielding', models.JSONField(default=dict)),
                ('pitching', models.JSONField(default=dict)),
                ('baserunning', models.JSONField(default=dict)),
                ('game_box_score', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lineup', to='baseball.teamboxscore')),
                ('team_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stats_by_game', to='baseball.teamplayer')),
            ],
            options={
                'verbose_name': 'Player Game Stats',
                'verbose_name_plural': 'Player Game Stats',
                'ordering': ['created'],
            },
        ),
    ]
