# Generated by Django 2.1.3 on 2019-04-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("data_import", "0017_auto_20190329_1638")]

    operations = [
        migrations.AlterField(
            model_name="awsdatafileaccesslog",
            name="bytes_sent",
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="awsdatafileaccesslog",
            name="object_size",
            field=models.BigIntegerField(null=True),
        ),
    ]