# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-20 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_review_commentcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='commentCategory',
            field=models.IntegerField(blank=True),
        ),
    ]
