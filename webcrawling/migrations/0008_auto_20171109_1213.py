# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawling', '0007_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hits',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
