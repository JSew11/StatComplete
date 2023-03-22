# Generated by Django 4.1.7 on 2023-03-22 15:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0017_competition_game_rules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('venue', models.JSONField(default=dict)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Scheduled'), (1, 'In Progress'), (2, 'Finished')], default=0)),
                ('rules', models.JSONField(default=dict)),
                ('competition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule', to='baseball.competition')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
                'ordering': ['created'],
            },
        ),
    ]
