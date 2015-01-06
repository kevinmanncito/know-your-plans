# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150105_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='copays',
            field=models.TextField(default=b'$100.00 office visit'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='family_deductable',
            field=models.DecimalField(default=100.0, max_digits=12, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='plan',
            name='individual_deductable',
            field=models.DecimalField(default=100.0, max_digits=12, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='plan',
            name='moop_family',
            field=models.DecimalField(default=100.0, max_digits=12, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='plan',
            name='moop_individual',
            field=models.DecimalField(default=100.0, max_digits=12, decimal_places=2),
        ),
    ]
