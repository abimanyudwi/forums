# Generated by Django 4.1.2 on 2023-05-16 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0019_alter_articlerequest_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="articlerequest",
            name="status",
            field=models.CharField(default="Diproses", max_length=400),
        ),
    ]
