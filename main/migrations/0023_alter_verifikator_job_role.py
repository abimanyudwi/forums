# Generated by Django 4.1.2 on 2023-05-18 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0022_alter_beverificator_options_beverificator_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="verifikator",
            name="job_role",
            field=models.CharField(default="Null", max_length=400),
        ),
    ]
