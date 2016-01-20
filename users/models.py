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
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django import forms
from django.forms import ModelForm
from utils.toolbox import string_random
from club.models import Club

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('User'), null=True)
    language = models.CharField(verbose_name=_(u'language'), max_length=8, choices=settings.LANGUAGES, default=1)
    current_club = models.ForeignKey(Club, verbose_name=_(u'Current club'), related_name='current_club', blank=True, null=True)
    clubs = models.ManyToManyField(Club, verbose_name=_(u'clubs'), related_name='clubs', blank=True)

    def __str__(self):
        return u"%s" % self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u, language=settings.LANGUAGES[0])[0])


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
