# Generated by Django 3.2.9 on 2021-11-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc_app', '0003_rename_updated_at_responsemodel_calculation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsemodel',
            name='calculation_time',
            field=models.CharField(max_length=100),
        ),
    ]
