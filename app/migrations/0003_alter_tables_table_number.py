# Generated by Django 4.0.4 on 2022-04-16 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tables',
            name='table_number',
            field=models.IntegerField(error_messages={'blank': 'Please enter table number'}, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
