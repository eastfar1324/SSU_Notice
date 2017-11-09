# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawling', '0006_auto_20171021_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_id', models.PositiveIntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('hits', models.PositiveIntegerField()),
            ],
        ),
    ]
