# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='orders_of_business',
            field=models.ManyToManyField(to='document.OrderOfBusiness', verbose_name='Orders of business', blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='president',
            field=models.ForeignKey(related_name='president', verbose_name='President', blank=True, to='club.Member'),
        ),
        migrations.AddField(
            model_name='club',
            name='reports',
            field=models.ManyToManyField(to='document.Report', verbose_name='Reports', blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='secretary',
            field=models.ForeignKey(related_name='secretary', verbose_name='Secretary', blank=True, to='club.Member'),
        ),
    ]
