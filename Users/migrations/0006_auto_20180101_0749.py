# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20171230_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nri',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
