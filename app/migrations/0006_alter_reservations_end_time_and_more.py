# Generated by Django 4.0.4 on 2022-04-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservations",
            name="end_time",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="reservations",
            name="start_time",
            field=models.DateField(),
        ),
    ]
