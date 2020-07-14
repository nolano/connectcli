#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'marcos santos'


from connect.conrequest import ConnectManager
from connect.conapi import ConnectApi

class App(object):
    
    @classmethod
    def list_apps(cls, limit, sort, filter_bundle_id = None):
        return ConnectManager().list_apps(ConnectApi.connect_api_apps.value, limit, sort, filter_bundle_id)