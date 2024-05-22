# Generated by Django 4.2.11 on 2024-05-09 13:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_b_form_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_fees',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='board_fees',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='examination_fees',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='monthly_fees',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='practical_fees',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]