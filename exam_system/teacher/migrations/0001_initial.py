# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-26 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('createtime', models.DateField(auto_now_add=True)),
                ('number', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Quess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField()),
                ('choise1', models.TextField()),
                ('choise2', models.TextField()),
                ('choise3', models.TextField()),
                ('choise4', models.TextField()),
                ('answer', models.CharField(max_length=10)),
                ('explain', models.TextField()),
                ('createdate', models.DateField(auto_now_add=True)),
                ('subid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Subjs')),
            ],
        ),
        migrations.CreateModel(
            name='Testinf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startime', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('deadline', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('classmsg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Classmsg')),
                ('paper', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.Papers')),
            ],
        ),
        migrations.AddField(
            model_name='papers',
            name='quess',
            field=models.ManyToManyField(to='teacher.Quess'),
        ),
        migrations.AddField(
            model_name='papers',
            name='subid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Subjs'),
        ),
    ]
