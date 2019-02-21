# Generated by Django 2.1.2 on 2019-02-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='true_distance',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='true_elevation',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=6, null=True),
        ),
    ]
