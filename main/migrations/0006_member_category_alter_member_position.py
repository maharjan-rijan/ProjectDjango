# Generated by Django 5.0.6 on 2024-07-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_rename_memberof_member_position"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="category",
            field=models.CharField(
                choices=[
                    ("electionOfficial", "electionOfficial"),
                    ("multipalStaffs", "multipalStaffs"),
                    ("wardMembers", "wardMembers"),
                ],
                default=None,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="member",
            name="position",
            field=models.CharField(
                choices=[
                    ("mayor", "mayor"),
                    ("deputy-mayor", "deputy-mayor"),
                    ("Deputy Secretary", "Deputy Secretary"),
                    ("Branch Officer", "Branch Officer"),
                    ("Accounts Officer", "Accounts Officer"),
                    ("engineer", "engineer"),
                ],
                default=None,
                max_length=50,
            ),
        ),
    ]
