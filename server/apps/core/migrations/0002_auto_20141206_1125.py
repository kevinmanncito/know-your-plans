# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='meta_info',
            field=models.ManyToManyField(to=b'core.PlanMetaInfo', null=True, blank=True),
        ),
    ]
