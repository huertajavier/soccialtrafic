# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 16:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171031_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
