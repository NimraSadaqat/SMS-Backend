# Generated by Django 4.2.11 on 2024-05-03 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=100)),
                ('father_nic_number', models.CharField(max_length=15)),
                ('father_occupation', models.CharField(max_length=100)),
                ('father_monthly_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('father_qualification', models.CharField(max_length=100)),
                ('father_address', models.TextField()),
                ('father_phone_number', models.CharField(max_length=15)),
                ('father_cell_number', models.CharField(max_length=15)),
                ('father_email', models.EmailField(max_length=254)),
                ('emergency_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.TextField()),
                ('religion', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=100)),
                ('last_school', models.TextField(blank=True, null=True)),
                ('date_of_admission', models.DateTimeField(auto_now_add=True)),
                ('admission_number', models.CharField(max_length=10)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.familyinformation')),
            ],
        ),
    ]