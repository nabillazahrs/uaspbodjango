# Generated by Django 4.1.2 on 2022-11-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("perpus_app", "0002_buku_kelompok_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="buku",
            name="img",
            field=models.CharField(max_length=40, null=True),
        ),
    ]