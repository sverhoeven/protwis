# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('protein', '0002_auto_20160926_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignprotStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PDB_code', models.CharField(max_length=4)),
                ('resolution', models.DecimalField(decimal_places=3, max_digits=5)),
                ('origin', models.ManyToManyField(to='protein.Protein')),
            ],
            options={
                'db_table': 'signprot_structure',
            },
        ),
    ]
