# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import address.models
import timezone_field.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('initial', models.CharField(max_length=10, verbose_name='Initial')),
                ('timezone', timezone_field.fields.TimeZoneField(default=b'Europe/Brussels')),
                ('telephone', models.CharField(blank=True, help_text='format : +32475123456', max_length=20, verbose_name='Telephone', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('address', address.models.AddressField(to='address.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='board_of_directors',
            field=models.ManyToManyField(related_name='board_of_directors', verbose_name='Board of directors', to='club.Member', blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(related_name='members', verbose_name='Members', to='club.Member', blank=True),
        ),
    ]
