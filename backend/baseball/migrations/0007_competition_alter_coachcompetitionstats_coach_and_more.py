# Generated by Django 4.1.6 on 2023-02-18 21:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0006_alter_coachcompetitionstats_coach_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Season'), (2, 'Tournament')], default=1)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Competition',
                'verbose_name_plural': 'Competitions',
                'ordering': ['created'],
            },
        ),
        migrations.AlterField(
            model_name='coachcompetitionstats',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stats_by_competition', to='baseball.coach'),
        ),
        migrations.AlterField(
            model_name='playercompetitionstats',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stats_by_competition', to='baseball.player'),
        ),
        migrations.AddField(
            model_name='coachcompetitionstats',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='coach_stats', to='baseball.competition'),
        ),
        migrations.AddField(
            model_name='playercompetitionstats',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player_stats', to='baseball.competition'),
        ),
    ]