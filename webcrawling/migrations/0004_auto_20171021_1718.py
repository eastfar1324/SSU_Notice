# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 17:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawling', '0003_auto_20171021_1648'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='Notice',
        ),
    ]
