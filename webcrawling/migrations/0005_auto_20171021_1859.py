# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawling', '0004_auto_20171021_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='categories',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='notice',
            name='owner',
            field=models.TextField(),
        ),
    ]
