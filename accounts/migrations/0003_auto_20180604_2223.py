# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-04 22:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180525_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10, 'Description must be at least 10 characters')]),
        ),
    ]
