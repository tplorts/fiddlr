# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fwa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='isOfficial',
            new_name='official',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='isPublic',
            new_name='public',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='isPublic',
            new_name='public',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='isPublic',
            new_name='public',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='isOfficial',
            new_name='official',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='isPublic',
            new_name='public',
        ),
        migrations.AddField(
            model_name='product',
            name='release',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
