# Generated by Django 4.2 on 2023-04-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rentalagreement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentalagreement',
            name='id',
        ),
        migrations.AlterField(
            model_name='rentalagreement',
            name='rentID',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]