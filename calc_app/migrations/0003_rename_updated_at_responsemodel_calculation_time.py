# Generated by Django 3.2.9 on 2021-11-09 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc_app', '0002_auto_20211109_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responsemodel',
            old_name='updated_at',
            new_name='calculation_time',
        ),
    ]
