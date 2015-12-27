# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.CharField(max_length=200)),
                ('loser', models.CharField(max_length=200)),
                ('gamename', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(verbose_name='created_on')),
                ('modified_on', models.DateTimeField(verbose_name='modified_on')),
            ],
        ),
    ]
