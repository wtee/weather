# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cancellations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancellation',
            name='details',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
