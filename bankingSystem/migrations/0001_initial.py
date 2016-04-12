# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-02 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(blank=True, max_length=16, null=True)),
                ('receiver', models.CharField(blank=True, max_length=16, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]