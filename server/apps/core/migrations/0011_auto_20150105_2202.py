# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150105_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantype',
            name='value',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
