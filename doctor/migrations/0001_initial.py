# Generated by Django 3.2 on 2022-09-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointments',
            fields=[
                ('appointment_id', models.UUIDField(primary_key=True, serialize=False)),
                ('patient_id', models.CharField(max_length=100)),
                ('doctor_id', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
                ('time_alloted', models.CharField(max_length=50)),
                ('number_alloted', models.CharField(max_length=50)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('is_disabled', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Doctor_profile',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=200)),
                ('hospital_id', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Doctor',
            },
        ),
        migrations.CreateModel(
            name='time_slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(max_length=100)),
                ('from_time', models.CharField(max_length=10)),
                ('to_time', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'time_slots',
            },
        ),
    ]
