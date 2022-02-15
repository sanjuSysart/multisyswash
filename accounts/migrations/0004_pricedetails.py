# Generated by Django 3.2.2 on 2022-02-11 06:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_clothdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceDetails',
            fields=[
                ('priceId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('price', models.IntegerField(blank=True)),
                ('xprice', models.IntegerField(blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('trash', models.BooleanField(default=False)),
                ('clothType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.clothdetails')),
                ('serviceName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.servicedetails')),
            ],
        ),
    ]