# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20171228_0928'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='NRI',
        ),
    ]
