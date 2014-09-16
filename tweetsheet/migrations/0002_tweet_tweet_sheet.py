# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweet_sheet',
            field=models.ForeignKey(default=1, to='tweetsheet.TweetSheet'),
            preserve_default=False,
        ),
    ]
