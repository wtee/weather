# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancellation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cancel_date', models.DateField()),
                ('type_of_cancel', models.CharField(default='Cancellation', max_length=50, choices=[('Cancellation', 'Cancellation'), ('Delay', 'Delay'), ('Early release', 'Early release'), ('Reschedule', 'Reschedule'), ('Other', 'Other')])),
                ('details', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('org_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
