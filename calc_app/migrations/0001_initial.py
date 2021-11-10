# Generated by Django 3.2.9 on 2021-11-09 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s', models.CharField(max_length=50)),
                ('v', models.CharField(max_length=50)),
                ('t', models.CharField(max_length=50)),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='calc_app.requestmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calculation_time', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='calc_app.requestmodel')),
            ],
        ),
    ]
