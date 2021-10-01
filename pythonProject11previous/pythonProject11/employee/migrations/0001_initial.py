# Generated by Django 3.1.7 on 2021-03-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=40)),
                ('employee_phone', models.CharField(max_length=11)),
                ('employee_email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='shipment',
            fields=[
                ('shipment_date', models.TextField()),
                ('tracking_number', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
    ]