# Generated by Django 4.1.1 on 2022-09-26 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AISite", "0011_visitor_delete_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="visitor",
            name="dob",
        ),
    ]