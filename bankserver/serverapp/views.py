#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from bankserver.serverapp.serializers import UserSerializer, GroupSerializer
from bankserver.serverapp.models import Transaction
from sendemail import SendEmail
from sendemail_valid import SendEmailValid
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import datetime
from rest_framework.permissions import AllowAny
from .permissions import IsStaffOrTargetUser
from rest_framework.decorators import api_view
from django.utils.crypto import get_random_string
from bankserver.serverapp.djangoemail import DjangoEmail
from django.shortcuts import render
from django.template.loader import get_template
from rest_framework.response import Response
from webserver.serverapp.transactionshash import TransctionHash
import random
import hashlib

try:
    from collections import OrderedDict
except ImportError:    
    from odict import odict as OrderedDict


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    model = User
 
    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class JSONResponse(HttpResponse):
    """docstring for JSONResponse"""
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['POST','GET'])
def bank_transaction(request):
    if request.user.is_authenticated():
        transactionhash = TransctionHash()
        for data in request.data:
            for key, value in data.items():
                key1 = transactionhash.decrypt(key, "fakher")
                value1 = transactionhash.decrypt(value, "fakher")
                data.append({key1: value1})
        data.append({'valid' : True}])
        print "Transaction Sent"
    else:
        print "Transaction not sent"
    return JSONResponse(data)

