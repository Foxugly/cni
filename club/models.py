# -*- coding: utf-8 -*-
#
# Copyright 2016, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from address.models import AddressField
from django.forms import ModelForm
from django import forms
from django.core.validators import RegexValidator
from document.models import Report, OrderOfBusiness
from timezone_field import TimeZoneField


class Member(models.Model):
    email = models.EmailField(verbose_name=_(u'Email address'), blank=False)
    first_name = models.CharField(verbose_name=_(u'First name'), max_length=50)
    last_name = models.CharField(verbose_name=_(u'Last name'), max_length=50)

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.email)

        
class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email']


class Club(models.Model):
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")
                                         
    name = models.CharField(verbose_name=_(u'Name'), max_length=255, blank=False, null=False)
    initial = models.CharField(verbose_name=_(u'Initial'), max_length=10, blank=False, null=False)
    address = AddressField()
    timezone = TimeZoneField(default=settings.TIME_ZONE)
    telephone = models.CharField(verbose_name=_(u'Telephone'), validators=[phone_regex],
                                 help_text=_(u'format : +32475123456'), max_length=20, blank=True)
    president = models.ForeignKey(Member, verbose_name=_(u'President'), related_name='president' , blank=True)
    secretary = models.ForeignKey(Member, verbose_name=_(u'Secretary'), related_name='secretary', blank=True)
    board_of_directors = models.ManyToManyField(Member, verbose_name=_(u'Board of directors'), related_name='board_of_directors',  blank=True)
    members = models.ManyToManyField(Member, verbose_name=_(u'Members'),  related_name='members', blank=True)
    orders_of_business = models.ManyToManyField(OrderOfBusiness, verbose_name=_(u'Orders of business'), blank=True)
    reports = models.ManyToManyField(Report, verbose_name=_(u'Reports'), blank=True)
    
    def __str__(self):
        return "%d %s" % (self.id, self.initial)

class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'initial', 'address', 'telephone', 'president', 'secretary', 'board_of_directors', 'members', 'orders_of_business', 'reports']
