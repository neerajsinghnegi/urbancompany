# Generated by Django 3.2.1 on 2021-11-09 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
    ]
