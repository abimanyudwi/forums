# Generated by Django 4.1.2 on 2023-05-16 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0017_remove_post_kategori_post_kategori"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="urutan",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
