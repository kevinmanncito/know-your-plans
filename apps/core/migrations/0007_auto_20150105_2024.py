# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_plan_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='plan',
        ),
        migrations.AddField(
            model_name='carrier',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='levels',
            field=models.ManyToManyField(to='core.Level', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plan',
            name='copays',
            field=models.TextField(default=b'100.00'),
        ),
    ]
