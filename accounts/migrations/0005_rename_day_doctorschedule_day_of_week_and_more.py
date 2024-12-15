# Generated by Django 5.1.3 on 2024-12-10 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_doctorschedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorschedule',
            old_name='day',
            new_name='day_of_week',
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor'),
        ),
    ]
