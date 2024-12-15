# Generated by Django 5.1.3 on 2024-12-08 06:40

import accounts.models
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBase',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('user_type', models.CharField(choices=[('ADMIN', 'admin'), ('DOCTOR', 'doctor'), ('PATIENT', 'patient')], max_length=10)),
                ('profile_image', models.ImageField(default='static/images/profile_images/default.jpeg', upload_to='static/images/profile_images/', validators=[accounts.models.validate_image_file])),
                ('id', models.CharField(editable=False, max_length=9, primary_key=True, serialize=False, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('userbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Administrator',
            },
            bases=('accounts.userbase',),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('userbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('license_number', models.CharField(max_length=255)),
                ('degree_certificate', models.FileField(blank=True, null=True, upload_to='static/certificates/', validators=[accounts.models.validate_pdf_file])),
                ('bio', models.TextField(blank=True)),
                ('specialty', models.CharField(choices=[('Dentist', 'Dentist'), ('Psychiatrist', 'Psychiatrist'), ('ENT', 'ENT')], max_length=50)),
            ],
            options={
                'verbose_name': 'Doctor',
            },
            bases=('accounts.userbase',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('userbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('medical_history_file', models.FileField(blank=True, null=True, upload_to='static/patients/medical_history/', validators=[accounts.models.validate_pdf_file])),
                ('date_of_birth', models.DateField()),
                ('storage_limit', models.BigIntegerField(default=52428800)),
                ('used_storage', models.BigIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Patient',
            },
            bases=('accounts.userbase',),
        ),
        migrations.CreateModel(
            name='DoctorPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('date_assigned', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_relationships', to='accounts.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_relationships', to='accounts.patient')),
            ],
            options={
                'unique_together': {('patient', 'doctor')},
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients',
            field=models.ManyToManyField(related_name='selected_doctors', through='accounts.DoctorPatient', to='accounts.patient'),
        ),
    ]
