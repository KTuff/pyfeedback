# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0030_remove_person_fachgebiet'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='fachgebiet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.Fachgebiet'),
        ),
    ]
