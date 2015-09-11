# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20150909_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blogapp.Tag'),
        ),
    ]
