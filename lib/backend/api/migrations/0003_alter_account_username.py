# Generated by Django 4.2 on 2023-05-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_account_password_alter_account_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
