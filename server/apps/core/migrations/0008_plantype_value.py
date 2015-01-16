# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150105_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantype',
            name='value',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
