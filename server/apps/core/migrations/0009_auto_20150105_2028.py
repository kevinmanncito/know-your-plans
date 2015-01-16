# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_plantype_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantype',
            name='value',
            field=models.CharField(max_length=255),
        ),
    ]
