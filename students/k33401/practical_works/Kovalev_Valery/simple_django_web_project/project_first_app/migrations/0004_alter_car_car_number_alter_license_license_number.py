# Generated by Django 4.1.2 on 2022-10-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_alter_own_end_own_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='license_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
