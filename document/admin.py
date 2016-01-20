# -*- coding: utf-8 -*-
#
# Copyright 2016, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib import admin
from document.models import Subject, Text, Point, Report, OrderOfBusiness


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    pass


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    pass


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    filter_horizontal = ['points', 'present_members', 'excused_members', 'missing_members']


@admin.register(OrderOfBusiness)
class OrderOfBusinessAdmin(admin.ModelAdmin):
    filter_horizontal = ['subjects']