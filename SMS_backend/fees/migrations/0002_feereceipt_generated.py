# Generated by Django 4.2.11 on 2024-05-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feereceipt',
            name='generated',
            field=models.BooleanField(default=False),
        ),
    ]