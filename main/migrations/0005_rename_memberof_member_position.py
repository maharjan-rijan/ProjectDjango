# Generated by Django 5.0.6 on 2024-07-15 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_about_contact_about_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="member",
            old_name="memberOf",
            new_name="position",
        ),
    ]