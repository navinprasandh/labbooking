# Generated by Django 3.2 on 2022-09-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('hos_id', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'Holidays',
            },
        ),
        migrations.CreateModel(
            name='Hospital_profile',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('beds_count', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Hospital',
            },
        ),
        migrations.CreateModel(
            name='Weekends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(max_length=50)),
                ('hos_id', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'Weekends',
            },
        ),
    ]
