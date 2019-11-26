#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'

import json,os,threading
from common import connectool
from common import netmanager
from connect.conapi import ConnectApi
from connect.contoken import ConnectToken

class SingletonMeta(type):
    __instance = None
    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = type.__call__(cls, *args, **kwargs)
        return cls.__instance


class ConnectManager(metaclass=SingletonMeta):
    def __init__(self):
        self.__token_object = None
    
    @property
    def tokenConfig(self):
        return self.__token_object
    
    @tokenConfig.setter
    def tokenConfig(self,token:ConnectToken):
        self.__token_object = token
    
    @property
    def __header(self):
        if not self.__token_object:
            raise Exception('token object not exist')
        return {"Authorization": 'Bearer '+self.__token_object.token}
    
    ## 注册udid
    # name 设备名
    # udid
    def register_device(self,url:str,name,udid):
        params = {'data':{'attributes':{'name':name,'udid':udid,'platform':'IOS'},'type':'devices'}}
        connectool.prints(url)
        connectool.prints(params)
        return netmanager.post(url,params=params,header=self.__header)
    
    ## 查询udid列表接口
    # limit 请求的udid个数
    # sort
    def list_devices(self,url:str,limit,sort):
        params = {'limit':limit,'sort':sort}
        connectool.prints(url)
        connectool.prints(self.__header)
        connectool.prints(params)
        return netmanager.get(url,params= params,header=self.__header)
    
    
    
    def register_bundle_id(self,url:str,bundle_id,team_id,name):
        params = {'data':{'attributes':{'identifier':bundle_id,'name':name,'platform':'IOS','seedId':team_id},'type':'bundleIds'}}
        connectool.prints(url)
        connectool.prints(params)
        return netmanager.post(url,params=params,header=self.__header)
    
    ## 查询bundleid列表接口
    # limit 请求的bundleid个数
    # sort Possible values: id, -id, name, -name, platform, -platform, seedId, -seedId
    def list_bundle_ids(self,url:str,limit,sort):
        params = {'limit':limit,'sort':sort}
        connectool.prints(url)
        connectool.prints(self.__header)
        connectool.prints(params)
        return netmanager.get(url,params= params,header=self.__header)
    
    ## 删除bundleid接口
    # id 
    def delete_bundle_id(self,url:str,id):
        connectool.prints(url)
        connectool.prints(self.__header)
        return netmanager.delete(url,path=id,header=self.__header)
    
    ## 获取bundleid信息
    # id 
    def get_bundle_id(self,url:str,id):
        url = url+'/'+id
        connectool.prints(url)
        connectool.prints(self.__header)
        return netmanager.get(url,header=self.__header)
    
    ## 获取bundleid profiles
    # id 
    def get_bundle_id_profiles(self,url:str,id):
        url = url+'/'+id+'/profiles'
        connectool.prints(url)
        connectool.prints(self.__header)
        return netmanager.get(url,header=self.__header)
    
     
    def register_certificate(self,url:str,csr,type):
        connectool.prints(url)
        params = {'data':{'attributes':{'certificateType':type,'csrContent':csr},'type':'certificates'}}
        connectool.prints(params)
        return netmanager.post(url,params=params,header=self.__header)
        
    ## 删除证书接口
    # id 
    def delete_certificate(self,url:str,id):
        connectool.prints(url)
        connectool.prints(self.__header)
        return netmanager.delete(url,path=id,header=self.__header)
            
    ## 查询证书
    # fields Possible values: certificateType, displayName, expirationDate, name
    # limit 请求的证书个数
    # sort Possible values: certificateType, -certificateType, displayName, -displayName, id, -id, serialNumber, -serialNumber
    def list_certificates(self,url:str,limit,sort):
        params = {'limit':limit,'sort':sort}
        connectool.prints(url)
        connectool.prints(self.__header)
        connectool.prints(params)
        return netmanager.get(url,params=params,header=self.__header)  
    
    ## 创建profile 文件
    # name profile name
    # profileType IOS_APP_DEVELOPMENT, IOS_APP_STORE, IOS_APP_ADHOC
    # bundle_id 包名的id
    # cerificate_id 证书id
    # devices
    def create_profile(self,url:str,name,type,bundle_id,cerificate_id,devices):
        params = {'data':{
                        'attributes':{'name':name,'profileType':type},
                        'relationships':{
                                            'bundleId':{'data':{'id':bundle_id,'type':'bundleIds'}},
                                            'certificates':{'data':[{'id':cerificate_id,'type':'certificates'}]},
                                            'devices':{'data':devices}},
                        'type':'profiles'
                    }
                }
        connectool.prints(url)
        connectool.prints(params)
        return netmanager.post(url,params=params,header=self.__header)              
    
    ## 删除profile接口
    # id 
    def delete_profile(self,url:str,id):
        connectool.prints(url)
        connectool.prints(self.__header)
        return netmanager.delete(url,path=id,header=self.__header)
    
    ## 查询profiles
    # limit 请求的profile个数
    # sort： id, -id, name, -name, profileState, -profileState, profileType, -profileType
    def list_profiles(self,url:str,limit,sort):
        params = {'limit':limit,'sort':sort}
        connectool.prints(url)
        connectool.prints(self.__header)
        connectool.prints(params)
        return netmanager.get(url,params=params,header=self.__header)  
    
    ## 查找profile
    # id
    def request_profile(self,url:str,id):
        url = url+'/'+id
        connectool.prints(url)
        connectool.prints(self.__header)
        return netmanager.get(url,header=self.__header) 
    

    
