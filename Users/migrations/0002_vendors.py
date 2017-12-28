# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('organization_email', models.CharField(max_length=100)),
            ],
        ),
    ]
