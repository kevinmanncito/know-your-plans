# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('cost', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member_number', models.CharField(unique=True, max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization_number', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('open_enroll_start', models.DateField()),
                ('open_enroll_end', models.DateField()),
                ('enroll_url', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_number', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('carrier', models.ForeignKey(to='core.Carrier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanMetaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SalesChannel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sales_channel_number', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='plan',
            name='meta_info',
            field=models.ManyToManyField(to='core.PlanMetaInfo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='organization',
            field=models.ForeignKey(to='core.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plan',
            name='plan_type',
            field=models.ForeignKey(to='core.PlanType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='sales_channel',
            field=models.ForeignKey(to='core.SalesChannel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='organization',
            field=models.ForeignKey(to='core.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='level',
            name='plan',
            field=models.ForeignKey(to='core.Plan'),
            preserve_default=True,
        ),
    ]
