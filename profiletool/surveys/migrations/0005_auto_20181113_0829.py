# Generated by Django 2.1.2 on 2018-11-13 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0004_auto_20181113_0828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reduced',
            old_name='station',
            new_name='station_id',
        ),
        migrations.RenameField(
            model_name='station',
            old_name='profile',
            new_name='profile_id',
        ),
    ]
