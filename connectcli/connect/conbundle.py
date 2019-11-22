#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'


from connect.conrequest import ConnectManager
from connect.conapi import ConnectApi

class BundleIdentifier(object):
    
    @classmethod
    def register_bundle_id(cls,bundle_id,team_id,name):
        result = ConnectManager().register_bundle_id(ConnectApi.connect_api_bundle_ids.value[0],bundle_id,team_id,name)
        if result['status'] == 201:
            return {'status':200,'data':result['data']}
        return result
    
    @classmethod
    def list_bundle_ids(cls,limit,sort):
        return ConnectManager().list_bundle_ids(ConnectApi.connect_api_bundle_ids.value[0],limit,sort)
     
    @classmethod
    def delete_bundle_id(cls,id):
        return ConnectManager().delete_bundle_id(ConnectApi.connect_api_bundle_ids.value[0],id)
    
    @classmethod
    def get_bundle_id(cls,id):
        return ConnectManager().get_bundle_id(ConnectApi.connect_api_bundle_ids.value[0],id)
    
    @classmethod
    def get_bundle_id_profiles(cls,id):
        return ConnectManager().get_bundle_id_profiles(ConnectApi.connect_api_bundle_ids.value[0],id)