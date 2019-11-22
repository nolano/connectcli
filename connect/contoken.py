#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'

from authlib.jose import jwt
import os
from datetime import datetime, timedelta
from common import connectool 

# key_id 密钥ID
# issuer_id 
# key_path 密钥文件路径
# expire_time 超时时间

class ConnectToken(object):
    def __init__(self,key_id,issuer_id,timeout,key_path=None):
        self.__keyId = key_id
        self.__issuerId = issuer_id
        self.__timeout = timeout
        self.__expire_time = 0
        self.__token = None
        self.__set_key_path(key_path)
        
    def __set_key_path(self,value):
        self.__key_path = None
        if value and os.path.exists(value):
            self.__key_path = value
        else :
            home = os.environ['HOME']
            for path in os.listdir(home):
                if 'private_keys' in path:
                    private_keys_path = os.path.join(home,path,'AuthKey_'+self.__keyId+'.p8')
                    if os.path.exists(private_keys_path):
                        self.__key_path = private_keys_path
                        connectool.prints(self.__key_path)
                        break
        if not self.__key_path:
            raise Exception('private_keys not exist')
        
    def __private_key(self):
        with open(self.__key_path,'r') as fp:
            try:
                return fp.read()
            except Exception as excep:
                connectool.prints(excep)
                
    @property
    def __is_expire(self):
        if datetime.now().timestamp()<self.__expire_time:
            return False
        return True
    
    @property
    def token(self)->str:
        if not self.__token or self.__is_expire:
            self.__expire_time = int((datetime.now()+timedelta(minutes=self.__timeout)).timestamp())
            self.__token = ConnectToken.encode(self.__keyId,self.__issuerId,self.__private_key(),self.__expire_time)
        return str(self.__token,encoding='utf-8')
    
    @classmethod
    def encode(cls,key_id,issuer_id,private_key,expire_time):
        payload = {'iss':issuer_id,
                   'exp':expire_time,
                   'aud':'appstoreconnect-v1'}
        result = jwt.encode(header={'kid':key_id,'typ':'JWT',"alg": "ES256"},payload=payload,key=private_key)
        return result