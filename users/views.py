
# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from users.models import UserProfile, UserCreateForm
from django.contrib.auth.forms import PasswordChangeForm
from utils.toolbox import string_random
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.conf import settings
from dateutil.relativedelta import relativedelta
from datetime import datetime, date
from utils.mail import mail_user_welcome
import json
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'dashboard.tpl')

@login_required
def password(request):
    results = {}
    if request.is_ajax():
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            results['return'] = True
        else:
            results['errors'] = form.errors
            results['return'] = False
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))