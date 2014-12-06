# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20141206_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='carrier',
            field=models.ForeignKey(related_name=b'plans', to='core.Carrier'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='organization',
            field=models.ForeignKey(related_name=b'plans', to='core.Organization'),
        ),
    ]
