# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-17 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingSystem', '0005_auto_20160408_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionConfirmLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('primary_account', models.CharField(blank=True, max_length=16, null=True)),
                ('secondary_account', models.CharField(blank=True, max_length=16, null=True)),
                ('time', models.FloatField(blank=True, null=True)),
                ('attempts', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('primary_account', models.CharField(blank=True, max_length=16, null=True)),
                ('secondary_account', models.CharField(blank=True, max_length=16, null=True)),
                ('time', models.FloatField(blank=True, null=True)),
                ('attempts', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
