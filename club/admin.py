# -*- coding: utf-8 -*-
#
# Copyright 2016, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib import admin
from club.models import Club, Member


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    filter_horizontal = ['board_of_directors', 'members', 'orders_of_business', 'reports']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass
