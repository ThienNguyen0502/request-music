# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_name', models.CharField(max_length=200, verbose_name=b'Song name')),
                ('url', models.TextField(verbose_name=b'URL')),
                ('source', models.CharField(default=b'From other (zing, nhaccuatui, ...)', max_length=50, choices=[(b'youtube', b'From youtube'), (b'other', b'From other (zing, nhaccuatui, ...)')])),
                ('author', models.CharField(max_length=200, verbose_name=b'Author')),
                ('pub_date', models.DateField(verbose_name=b'Play on')),
            ],
            options={
                'ordering': ['song_name'],
                'verbose_name': 'song',
            },
        ),
    ]
