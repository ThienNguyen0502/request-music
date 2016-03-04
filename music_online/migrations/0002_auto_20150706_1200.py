# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_online', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='message',
            field=models.TextField(verbose_name=b'Message', blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='source',
            field=models.CharField(default=b'other', max_length=50, choices=[(b'youtube', b'From youtube'), (b'other', b'From zing or nhaccuatui')]),
        ),
    ]
