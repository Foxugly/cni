# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django import template
import os
from datetime import datetime
# from utils.toolbox import reformat_date
from django.utils import formats


register = template.Library()


@register.filter()
def index(d, value):
    return dict(d)[value]


@register.filter()
def time_format(time):
    return u"%02d:%02d" % (time.hour, time.minute)


@register.filter()
def date_format(date):
    return date.strftime(formats.get_format('DATE_INPUT_FORMATS')[0])


@register.filter()
def filename(path):
    return os.path.basename(path.name)


@register.filter()
def cast(s):
    return s.replace(' ', '+')


@register.filter()
def after_today(date):
    return date > datetime.today()


@register.filter()
def file_exists(path):
    if path:
        return os.path.exists(path)
    else:
        return False
