# Generated by Django 3.2.9 on 2021-11-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc_app', '0005_auto_20211109_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rowmodel',
            name='s',
            field=models.FloatField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rowmodel',
            name='t',
            field=models.FloatField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rowmodel',
            name='v',
            field=models.FloatField(max_length=50),
        ),
    ]