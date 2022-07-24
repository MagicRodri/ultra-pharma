# Generated by Django 3.2.13 on 2022-07-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220723_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('DIRECTOR', 'Director'), ('MANAGER', 'Manager'), ('EMPLOYEE', 'Employee'), ('CUSTOMER', 'Customer')], default='DEFAULT', max_length=25),
        ),
    ]