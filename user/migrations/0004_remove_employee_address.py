# Generated by Django 3.2.1 on 2021-11-10 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_employee_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
    ]
