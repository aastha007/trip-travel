# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-17 07:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0006_auto_20170717_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countries',
            old_name='About',
            new_name='C_About',
        ),
        migrations.RenameField(
            model_name='countries',
            old_name='Name',
            new_name='C_Name',
        ),
    ]
