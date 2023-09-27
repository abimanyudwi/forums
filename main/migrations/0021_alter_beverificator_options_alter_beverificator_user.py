# Generated by Django 4.1.2 on 2023-05-16 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0020_articlerequest_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="beverificator",
            options={"verbose_name_plural": "BeVerifikator"},
        ),
        migrations.AlterField(
            model_name="beverificator",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.author"
            ),
        ),
    ]
