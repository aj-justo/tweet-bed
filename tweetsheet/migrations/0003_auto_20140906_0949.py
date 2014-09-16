# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsheet', '0002_tweet_tweet_sheet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweetsheet',
            old_name='hashtags',
            new_name='hash_tags',
        ),
        migrations.AddField(
            model_name='tweetsheet',
            name='title',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
