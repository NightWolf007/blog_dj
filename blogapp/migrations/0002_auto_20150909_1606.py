# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
