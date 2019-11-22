#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'

base_api = 'https://api.appstoreconnect.apple.com/v1/'

from enum import Enum, unique

@unique
class ConnectApi(Enum):
    #设备
    connect_api_devices = base_api+'devices',
    
    # 包名
    connect_api_bundle_ids = base_api+'bundleIds',
    
    #证书
    connect_api_certificates = base_api+'certificates',
    
    #provision file
    connect_api_profiles = base_api+'profiles',
    
    # 财务报告
    connect_api_financeReports = base_api+'financeReports'
    
    