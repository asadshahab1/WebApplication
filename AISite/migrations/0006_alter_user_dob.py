# Generated by Django 4.1.1 on 2022-09-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AISite", "0005_alter_user_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="dob",
            field=models.DateField(default=1990),
        ),
    ]