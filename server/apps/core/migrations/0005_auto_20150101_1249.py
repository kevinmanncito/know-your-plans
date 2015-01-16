# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150101_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='mmop_family',
            new_name='moop_family',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='mmop_individual',
            new_name='moop_individual',
        ),
    ]
