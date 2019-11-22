#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'
import os
from common import connectool
from connect.conrequest import ConnectManager
from connect.conapi import ConnectApi


class Certificate(object):
    @classmethod
    def get_certSigningRequest(cls,path=None):
        if path:
            return connectool.loadFile(path)
    
    @classmethod
    def register_certificate(cls,out_path,csr_path,type):
        csr = Certificate.get_certSigningRequest(path=csr_path)
        result = ConnectManager().register_certificate(ConnectApi.connect_api_certificates.value[0],csr,type=type)
        if result['status'] == 201:
            res = result["data"]['data']
            file_path = os.path.join(out_path,res['id']+'.cer')
            decode_content = connectool.base64decode(res['attributes']['certificateContent'])
            connectool.saveByteFile(decode_content,file_path)
            return {'status':200,'path':file_path,'data':result['data']}
        return result
    
    @classmethod
    def delete_certificate(cls,id):
        return ConnectManager().delete_certificate(ConnectApi.connect_api_certificates.value[0],id)
    
    @classmethod
    def list_cerificate(cls,limit,sort):
        return ConnectManager().list_certificates(ConnectApi.connect_api_certificates.value[0],limit,sort)