# Generated by Django 4.1.1 on 2022-09-25 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AISite", "0002_user_first_name_user_last_name_user_phone_no_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="dob",
            field=models.DateField(default="2022-02-12"),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(default="", max_length=10),
        ),
    ]
