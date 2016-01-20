# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import address.models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderOfBusiness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='Order of Business', max_length=255, verbose_name='Name')),
                ('meeting_datetime', models.DateTimeField(verbose_name='Date of the meeting')),
                ('timezone', timezone_field.fields.TimeZoneField(default=b'Europe/Brussels')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('address', address.models.AddressField(to='address.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='Report', max_length=255, verbose_name='Name')),
                ('datetime', models.DateTimeField(verbose_name='Datetime')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('excused_members', models.ManyToManyField(related_name='excused_members', verbose_name='Excused Members', to='club.Member', blank=True)),
                ('missing_members', models.ManyToManyField(related_name='missing_members', verbose_name='Missing Members', to='club.Member', blank=True)),
                ('order_of_business', models.ForeignKey(verbose_name='Order of business', blank=True, to='document.OrderOfBusiness')),
                ('points', models.ManyToManyField(to='document.Point', verbose_name='Points', blank=True)),
                ('present_members', models.ManyToManyField(related_name='present_members', verbose_name='Present Members', to='club.Member', blank=True)),
                ('reporter', models.ForeignKey(related_name='reporter', verbose_name='reporter', blank=True, to='club.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True, verbose_name='Text', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='subject',
            field=models.ForeignKey(verbose_name='Subject', to='document.Subject'),
        ),
        migrations.AddField(
            model_name='point',
            name='text',
            field=models.ForeignKey(verbose_name='Text', blank=True, to='document.Text'),
        ),
        migrations.AddField(
            model_name='orderofbusiness',
            name='subjects',
            field=models.ManyToManyField(to='document.Subject', verbose_name='Subjects', blank=True),
        ),
    ]
