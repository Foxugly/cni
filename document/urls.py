# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls import url
from document.views import oob_add, oob_view
from django.contrib.auth.decorators import login_required

urlpatterns = (
    url(r'^oob/add/$', login_required(oob_add), name='oob_add'),
    url(r'^oob/(?P<id>[\w-]+)/$', login_required(oob_view), name='oob_view'),

)