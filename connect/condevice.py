
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'
from connect.conrequest import ConnectManager
from connect.conapi import ConnectApi


class Device(object):
    
    @classmethod    
    def regist_device(cls,name,udid):
        return ConnectManager().register_device(ConnectApi.connect_api_devices.value[0],name,udid)
    
    @classmethod
    def list_devices(cls,limit,sort):
        result = ConnectManager().list_devices(ConnectApi.connect_api_devices.value[0],limit,sort)
        if result['status'] == 200:
            return{'status':200,'data':result['data']['data']}
        return result