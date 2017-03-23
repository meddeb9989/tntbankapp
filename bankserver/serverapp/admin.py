#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from bankserver.serverapp.models import Transaction


admin.site.register(Transaction)
AdminSite.site_title = ugettext_lazy('TAN & TECH ADMIN')
AdminSite.site_header = ugettext_lazy('TAN & TECH ADMINISTRATION')
AdminSite.index_title = ugettext_lazy('DATA BASE ADMINISTRATION')

