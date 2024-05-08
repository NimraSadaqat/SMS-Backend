# Generated by Django 4.2.11 on 2024-05-08 12:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic_year', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=100)),
                ('father_nic_number', models.CharField(max_length=15)),
                ('father_occupation', models.CharField(max_length=100)),
                ('father_monthly_income', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(1000000)])),
                ('father_qualification', models.CharField(max_length=100)),
                ('father_address', models.TextField()),
                ('father_cell_number', models.CharField(max_length=12)),
                ('status', models.CharField(choices=[('current', 'Current'), ('left', 'Left')], default='current', max_length=7)),
                ('father_phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('father_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('father_office_address', models.TextField(blank=True, null=True)),
                ('father_office_number', models.CharField(blank=True, max_length=12, null=True)),
                ('mother_name', models.CharField(max_length=100)),
                ('mother_nic_number', models.CharField(max_length=15)),
                ('mother_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_monthly_income', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(1000000)])),
                ('mother_qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_address', models.TextField(blank=True, null=True)),
                ('mother_phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('mother_cell_number', models.CharField(blank=True, max_length=12, null=True)),
                ('emergency_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.TextField()),
                ('religion', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=100)),
                ('b_form_number', models.CharField(max_length=15)),
                ('last_school', models.TextField(blank=True, null=True)),
                ('date_of_admission', models.DateField(auto_now_add=True)),
                ('admitted_in_grade', models.CharField(choices=[('Be', 'Beginner'), ('El', 'Elementary'), ('Pr', 'Prep'), ('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five'), ('6', 'Six'), ('7', 'Seven'), ('8', 'Eight'), ('IX', 'Nine'), ('X', 'Matric')], max_length=2)),
                ('status', models.CharField(choices=[('current', 'Current'), ('left', 'Left')], default='current', max_length=7)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='A', max_length=1)),
                ('roll_number', models.CharField(max_length=5)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('monthly_fees', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('admission_fees', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('examination_fees', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('board_fees', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('practical_fees', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('last_updated', models.DateField(auto_now=True)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_year.academic_year')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.familyinformation')),
            ],
        ),
    ]
