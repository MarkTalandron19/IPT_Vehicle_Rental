# Generated by Django 4.2 on 2023-04-30 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('accountID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('accountRole', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicleID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('vehicleName', models.CharField(max_length=100)),
                ('vehicleModel', models.CharField(max_length=100)),
                ('vehicleBrand', models.CharField(max_length=100)),
                ('vehicleManufacturer', models.CharField(max_length=100)),
                ('vehicleType', models.CharField(max_length=100)),
                ('vehicleRentRate', models.FloatField()),
                ('available', models.BooleanField(default=True)),
                ('image', models.CharField(default=None, max_length=1000)),
            ],
            options={
                'db_table': 'vehicle',
            },
        ),
        migrations.CreateModel(
            name='RentalAgreement',
            fields=[
                ('rentID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('rentDate', models.DateField()),
                ('numberOfDays', models.PositiveIntegerField()),
                ('rentDue', models.FloatField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle')),
            ],
            options={
                'db_table': 'rental_agreement',
            },
        ),
    ]
