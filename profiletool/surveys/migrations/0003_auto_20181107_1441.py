# Generated by Django 2.1.2 on 2018-11-07 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20181107_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='elevation_control',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number_of_stations',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='survey_instance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='surveys.Survey'),
        ),
        migrations.AlterField(
            model_name='station',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surveys.Profile'),
        ),
    ]
