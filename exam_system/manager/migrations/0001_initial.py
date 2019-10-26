# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-26 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classmsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=32)),
                ('regdate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(max_length=32)),
                ('premission', models.SmallIntegerField()),
                ('possword', models.CharField(max_length=32)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=16)),
                ('stuid', models.IntegerField(primary_key=True, serialize=False)),
                ('school', models.CharField(blank=True, max_length=32)),
                ('major', models.CharField(blank=True, max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('possword', models.CharField(max_length=32)),
                ('classid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.Classmsg')),
            ],
        ),
        migrations.CreateModel(
            name='Subjs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('possword', models.CharField(max_length=32)),
            ],
        ),
    ]
