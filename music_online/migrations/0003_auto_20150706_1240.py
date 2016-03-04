# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_online', '0002_auto_20150706_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='author',
        ),
        migrations.AddField(
            model_name='song',
            name='sender',
            field=models.CharField(default='', max_length=200, verbose_name=b'Sender'),
            preserve_default=False,
        ),
    ]
