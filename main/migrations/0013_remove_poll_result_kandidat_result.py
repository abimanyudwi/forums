# Generated by Django 4.1.2 on 2022-11-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_poll_result"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="poll",
            name="result",
        ),
        migrations.AddField(
            model_name="kandidat",
            name="result",
            field=models.ManyToManyField(blank=True, to="main.pollresult"),
        ),
    ]
