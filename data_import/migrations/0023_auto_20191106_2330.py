# Generated by Django 2.2.3 on 2019-11-06 23:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("data_import", "0022_auto_20191105_1924")]

    operations = [
        migrations.AlterField(
            model_name="datatype",
            name="description",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="datatype",
            name="name",
            field=models.CharField(
                max_length=40,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[\\w\\-\\s]+$",
                        "Only alphanumeric characters, space, dash, and underscore are allowed.",
                    )
                ],
            ),
        ),
    ]
