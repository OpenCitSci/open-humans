# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 18:40
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pgp', '0005_remove_datafile_subtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='metadata',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
