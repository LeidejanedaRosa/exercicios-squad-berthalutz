# Generated by Django 4.2.11 on 2024-04-08 01:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_register_book"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cadastro",
            options={
                "ordering": ["-data_cadastro"],
                "verbose_name": "Cadastro",
                "verbose_name_plural": "Cadastros",
            },
        ),
    ]