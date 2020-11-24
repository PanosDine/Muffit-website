# Generated by Django 3.1.3 on 2020-11-24 12:30

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('postcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50, unique=True)),
                ('phone', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Muffin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muffin_name', models.CharField(max_length=50, unique=True)),
                ('muffin_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=50, unique=True)),
                ('reference_code', models.CharField(default=api.models.generate_unique_code, max_length=6, unique=True)),
                ('delivery_address', models.CharField(max_length=50)),
                ('delivery_date', models.DateTimeField(verbose_name='Delivery date & time')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('muffin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.muffin')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
    ]
