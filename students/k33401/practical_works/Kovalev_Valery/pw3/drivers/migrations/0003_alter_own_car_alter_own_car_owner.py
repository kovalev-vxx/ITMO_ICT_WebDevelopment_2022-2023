# Generated by Django 4.1.4 on 2023-01-16 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_alter_license_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='own',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='own', to='drivers.car'),
        ),
        migrations.AlterField(
            model_name='own',
            name='car_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='own', to='drivers.carowner'),
        ),
    ]