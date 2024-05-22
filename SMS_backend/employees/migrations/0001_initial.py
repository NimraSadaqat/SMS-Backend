# Generated by Django 4.2.11 on 2024-05-09 06:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nic_number', models.CharField(max_length=15)),
                ('qualification', models.TextField()),
                ('address', models.TextField()),
                ('cell_number', models.CharField(max_length=12)),
                ('status', models.CharField(choices=[('current', 'Current'), ('left', 'Left')], default='current', max_length=7)),
                ('phone_number1', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number2', models.CharField(blank=True, max_length=12, null=True)),
                ('emergency_number', models.CharField(blank=True, max_length=15, null=True)),
                ('joined_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)])),
                ('absents', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('late_commings', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('date', models.DateField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employeeinformation')),
            ],
        ),
    ]
