# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-26 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classmsg',
            options={'verbose_name': 'Classmsg'},
        ),
        migrations.AlterField(
            model_name='classmsg',
            name='classname',
            field=models.CharField(max_length=32, verbose_name='classname'),
        ),
    ]
