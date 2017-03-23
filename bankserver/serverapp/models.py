#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db import models


class Transaction(models.Model):
    id_employe = models.IntegerField()
    id_commercant = models.IntegerField()
    date = models.DateTimeField()
    confirmed = models.BooleanField(default=False)
    montant = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return "Transaction : "+ str(date) + " : Confirmed : " + str(confirmed) + " : Montant : " + str(montant)

