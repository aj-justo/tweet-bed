# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsheet', '0005_auto_20140906_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetsheet',
            name='header_image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
