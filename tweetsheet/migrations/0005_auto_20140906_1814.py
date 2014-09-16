# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsheet', '0004_tweet_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='number',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_sheet',
            field=models.ForeignKey(related_name=b'tweets', to='tweetsheet.TweetSheet'),
        ),
    ]
