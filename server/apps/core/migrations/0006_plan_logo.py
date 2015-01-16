# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150101_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
