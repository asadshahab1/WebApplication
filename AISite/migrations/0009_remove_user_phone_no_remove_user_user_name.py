# Generated by Django 4.1.1 on 2022-09-25 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AISite", "0008_alter_user_dob"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="phone_no",
        ),
        migrations.RemoveField(
            model_name="user",
            name="user_name",
        ),
    ]
