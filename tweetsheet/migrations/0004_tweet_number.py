# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsheet', '0003_auto_20140906_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='number',
            field=models.SmallIntegerField(help_text=b'Optional. Order of the tweet in the tweet sheet. It will be assigned automatically if left blank.', null=True, blank=True),
            preserve_default=True,
        ),
    ]
