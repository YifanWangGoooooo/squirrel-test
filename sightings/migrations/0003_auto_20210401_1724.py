# Generated by Django 3.1.7 on 2021-04-01 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_auto_20210401_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='approaches',
            new_name='Approaches',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='chasing',
            new_name='Chasing',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='climbing',
            new_name='Climbing',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='eating',
            new_name='Eating',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='foraging',
            new_name='Foraging',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='indifferent',
            new_name='Indifferent',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='kuks',
            new_name='Kuks',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='latitude',
            new_name='Latitude',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='longitude',
            new_name='Longitude',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='moans',
            new_name='Moans',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='other_activities',
            new_name='Other_Activities',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='quaas',
            new_name='Quaas',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='running',
            new_name='Running',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='runs_from',
            new_name='Runs_From',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='tail_flags',
            new_name='Tail_Flags',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='tail_twitches',
            new_name='Tail_Twitches',
        ),
    ]
