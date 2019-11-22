#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'
import os
from connect.conrequest import ConnectManager
from connect.conapi import ConnectApi
from common import connectool

class Profile(object):
    
    ## 创建profile 文件
    # name profile name
    # type IOS_APP_DEVELOPMENT, IOS_APP_STORE, IOS_APP_ADHOC
    # bundle_id 包名的id
    # certificate_id 证书id
    # devices
    @classmethod
    def create_profile(cls,name,bundle_id,certificate_id,devices,type,out_path):
        result = ConnectManager().create_profile(ConnectApi.connect_api_profiles.value[0],name=name,bundle_id=bundle_id,cerificate_id=certificate_id,devices=devices,type=type)
        if result['status'] == 201:
            res = result['data']['data']['attributes']
            path = os.path.join(out_path,res['uuid']+'.mobileprovision')
            decode_content = connectool.base64decode(res['profileContent'])
            connectool.saveByteFile(decode_content,path)
            return {'status':200,'data':result['data']['data'],'path':path}
        return result
    
    ## 删除profile接口
    # id 
    @classmethod
    def delete_profile(cls,id):
        return ConnectManager().delete_profile(ConnectApi.connect_api_profiles.value[0],id)
    
    ## 查询profiles
    # limit 请求的profile个数
    # sort： id, -id, name, -name, profileState, -profileState, profileType, -profileType
    @classmethod
    def list_profiles(cls,limit,sort):
        return ConnectManager().list_profiles(ConnectApi.connect_api_profiles.value[0],limit = limit,sort=sort)
    
    ## 查找profile
    # id
    @classmethod
    def request_profile(cls,id):
        return ConnectManager().request_profile(ConnectApi.connect_api_profiles.value[0],id)