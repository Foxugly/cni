# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(default=1, max_length=8, verbose_name='language', choices=[(b'fr', 'Francais'), (b'nl', 'Nederlands'), (b'en', 'English')])),
                ('clubs', models.ManyToManyField(related_name='clubs', verbose_name='clubs', to='club.Club', blank=True)),
                ('current_club', models.ForeignKey(related_name='current_club', verbose_name='Current club', blank=True, to='club.Club', null=True)),
                ('user', models.OneToOneField(null=True, verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
