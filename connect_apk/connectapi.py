#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'

import os
from connect.contoken import ConnectToken
from connect.conrequest import ConnectManager
from connect.condevice import Device
from connect.concertificate import Certificate
from connect.conbundle import BundleIdentifier
from connect.conprofile import Profile

class ConnectApi(object):
    ## 初始化方法
    # api_key 
    # issuer_id
    # private_path
    def __init__(self,api_key,issuer_id,private_path=None,timeout=15):
        token_object = ConnectToken(api_key,issuer_id,key_path=private_path,timeout=timeout)
        ConnectManager().tokenConfig = token_object
        
    ## 注册设备
    # name 设备名
    # udid 设备唯一标识
    def register_device(self,name,udid):
        return Device.regist_device(name,udid)
    
    ##设备列表
    def list_devices(self,limit=100,sort='id'):
        return Device.list_devices(limit,sort)
    
    ## 注册证书
    # type 证书类型 IOS_DEVELOPMENT｜IOS_DISTRIBUTION
    # csr_path 证书请求文件路径
    # out_path 输出路径
    def register_certificate(self,csr_path=None,out_path=os.environ['HOME'],type='IOS_DEVELOPMENT'):
        return Certificate.register_certificate(out_path=out_path,csr_path=csr_path,type=type)
    
    #删除证书
    # id 证书id
    def delete_certificate(self,id):
        return Certificate.delete_certificate(id)
    
    ## 查询证书
    # fields Possible values: certificateType, displayName, expirationDate, name
    # limit 请求的证书个数
    # sort Possible values: certificateType, -certificateType, displayName, -displayName, id, -id, serialNumber, -serialNumber
    def list_certificates(self,limit=100,sort='id'):
        return Certificate.list_cerificate(limit,sort)
    
    ## 注册bundle id
    # bundle_id 包名（app 唯一标识）
    # team_id 开发者唯一标识
    # name bunle_id 别名
    def register_bundle_id(self,bundle_id,team_id,name):
        return BundleIdentifier.register_bundle_id(bundle_id,team_id,name)
    
    ## 查询bundleid列表接口
    # limit 请求的bundleid个数
    # sort Possible values: id, -id, name, -name, platform, -platform, seedId, -seedId
    def list_bundle_ids(self,limit=100,sort='id'):
        return BundleIdentifier.list_bundle_ids(limit,sort)
     
    ## 删除bundleid接口
    # id 
    def delete_bundle_id(self,id):
        return BundleIdentifier.delete_bundle_id(id)
    
    ## 获取bundleid信息
    # id
    def get_bundle_id(self,id):
        return BundleIdentifier.get_bundle_id(id)
    
    ## 获取bundleid profiles
    # id 
    def get_bundle_id_profiles(self,id):
        return BundleIdentifier.get_bundle_id_profiles(id)
    
    
    ## 创建profile 文件
    # name profile name
    # type IOS_APP_DEVELOPMENT, IOS_APP_STORE, IOS_APP_ADHOC
    # bundle_id 包名的id
    # certificate_id 证书id
    # devices
    def create_profile(self,name,bundle_id,certificate_id,devices=[],type='IOS_APP_ADHOC',out_path=os.environ['HOME']):
        if len(devices)==0:
            result = self.list_devices()
            if result['status'] == 200:
                for info in result['data']:
                    devices.append({'id':info['id'],'type':info['type']})
                if len(devices)==0:
                    return {'status':'400','data':'don\'t have any devices'}
            else:
                return result
        return Profile.create_profile(name,bundle_id,certificate_id,devices,type,out_path)
        
    ## 删除profile接口
    # id 
    def delete_profile(self,id):
        return Profile.delete_profile(id)
    
    ## 查询profiles
    # limit 请求的profile个数
    # sort： id, -id, name, -name, profileState, -profileState, profileType, -profileType
    def list_profiles(self,limit=100,sort='id'):
        return Profile.list_profiles(limit,sort)
    
    ## 查找profile
    # id
    def request_profile(self,id):
        return Profile.request_profile(id)
        