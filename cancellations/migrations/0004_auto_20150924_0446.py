# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cancellations', '0003_cancellation_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='org_type',
            field=models.CharField(choices=[('School', 'School'), ('Business', 'Business'), ('Community Organization', 'Community Organization'), ('Other', 'Other')], max_length=50, default='School'),
        ),
        migrations.RemoveField(
            model_name='cancellation',
            name='organization',
        ),
        migrations.AddField(
            model_name='cancellation',
            name='organization',
            field=models.ForeignKey(default=1, to='cancellations.Organization'),
            preserve_default=False,
        ),
    ]
