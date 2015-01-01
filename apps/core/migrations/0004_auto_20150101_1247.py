# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141206_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='co_insurance',
            field=models.DecimalField(default=1.0, max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='copays',
            field=models.CharField(default=b'100.00', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='family_deductable',
            field=models.DecimalField(default=1.0, max_digits=12, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='individual_deductable',
            field=models.DecimalField(default=1.0, max_digits=12, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='mmop_family',
            field=models.DecimalField(default=1.0, max_digits=12, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='mmop_individual',
            field=models.DecimalField(default=1.0, max_digits=12, decimal_places=2),
            preserve_default=True,
        ),
    ]
