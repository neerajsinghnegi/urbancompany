# Generated by Django 3.2.1 on 2021-11-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_choose_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choose',
            name='status',
            field=models.TextField(blank=True, default='Not replied'),
        ),
    ]
