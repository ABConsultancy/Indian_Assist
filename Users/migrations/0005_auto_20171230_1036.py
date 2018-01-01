# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20171228_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='nri',
            name='budget',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='nri',
            name='email_address',
            field=models.EmailField(max_length=100),
        ),
    ]
