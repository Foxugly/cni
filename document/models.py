# -*- coding: utf-8 -*-
#
# Copyright 2016, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from django import forms
from django.conf import settings
from timezone_field import TimeZoneField
from address.models import AddressField


class Subject(models.Model):
    subject = models.CharField(verbose_name=_(u'Subject'), max_length=255)

    def __str__(self):
        return "%d %s" % (self.id, self.subject)

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['subject']
        

class Text(models.Model):
    text = models.TextField(verbose_name=_(u'Text'), blank=True, null=True)

    def __str__(self):
        return u"%d %s" % (self.id, self.text)

class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = ['text']


class Point(models.Model):
    subject = models.ForeignKey(Subject, verbose_name=_(u'Subject'), blank=False)
    text = models.ForeignKey(Text, verbose_name=_(u'Text'), blank=True)

    def __str__(self):
        return u"%d %s" % (self.id, self.subject)

class PointForm(ModelForm):
    class Meta:
        model = Point
        fields = ['subject', 'text']


class OrderOfBusiness(models.Model):
    name = models.CharField(verbose_name=_(u'Name'), max_length=255, default=_(u'Order of Business'))
    meeting_datetime = models.DateTimeField(verbose_name=_(u'Date of the meeting'), blank=False)
    timezone = TimeZoneField(default=settings.TIME_ZONE)
    address = AddressField()
    date_creation = models.DateField(verbose_name=_(u'Creation date'), auto_now_add=True)
    subjects = models.ManyToManyField(Subject, verbose_name=_(u'Subjects'), blank=True)

    def __str__(self):
        return u"%s %s" % (self.name, self.meeting_datetime)


class OrderOfBusinessForm(ModelForm):
    class Meta:
        model = OrderOfBusiness
        fields = ['name', 'meeting_datetime', 'address']


class Report(models.Model):
    name = models.CharField(verbose_name=_(u'Name'), max_length=255, default=_(u'Report'))
    datetime = models.DateTimeField(verbose_name=_(u'Datetime'), blank=False)
    date_creation = models.DateField(verbose_name=_(u'Creation date'), auto_now_add=True)
    order_of_business = models.ForeignKey(OrderOfBusiness, verbose_name=_(u'Order of business'), blank=True)
    points = models.ManyToManyField(Point, verbose_name=_(u'Points'), blank=True)
    date_creation = models.DateField(verbose_name=_(u'Creation date'), auto_now_add=True)
    present_members = models.ManyToManyField('club.Member', verbose_name=_(u'Present Members'), related_name='present_members', blank=True)
    excused_members = models.ManyToManyField('club.Member', verbose_name=_(u'Excused Members'), related_name='excused_members',  blank=True)
    missing_members = models.ManyToManyField('club.Member', verbose_name=_(u'Missing Members'), related_name='missing_members',  blank=True)
    reporter = models.ForeignKey('club.Member', verbose_name=_(u'reporter'), related_name='reporter',  blank=True)
    
    def __str__(self):
        return u"%s %s" % (self.name, self.datetime)

#class ReportForm(ModelForm):
#    class Meta:
#        model = Report
#        exclude = ['date_creation']