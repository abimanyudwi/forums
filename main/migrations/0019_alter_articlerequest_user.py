# Generated by Django 4.1.2 on 2023-05-16 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0018_category_urutan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlerequest",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.author"
            ),
        ),
    ]
