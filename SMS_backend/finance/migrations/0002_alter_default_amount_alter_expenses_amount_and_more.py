# Generated by Django 4.0 on 2024-08-22 06:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='default',
            name='amount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000)]),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)]),
        ),
        migrations.AlterField(
            model_name='monthlyincome',
            name='amount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000)]),
        ),
    ]