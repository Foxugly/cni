# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderofbusiness',
            name='meeting_datetime',
        ),
        migrations.AddField(
            model_name='orderofbusiness',
            name='meeting_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 20, 21, 25, 20, 517280, tzinfo=utc), verbose_name='Date of the meeting'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderofbusiness',
            name='meeting_time',
            field=models.TimeField(default=datetime.datetime(2016, 1, 20, 21, 25, 30, 304782, tzinfo=utc), verbose_name='Time of the meeting'),
            preserve_default=False,
        ),
    ]
