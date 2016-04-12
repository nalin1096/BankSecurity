# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-08 01:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankingSystem', '0004_transaction_balance_remaining'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='receiver',
            new_name='primary_account',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='sender',
            new_name='secondary_account',
        ),
    ]
