#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'

import requests
from requests import Response

def get(url,params=None,header={}):
    res = requests.get(url,params=params,headers=header)
    json = res.json()
    if res.status_code == 200:
        return {'status':200,'msg':'','data':json}
    return {'status':res.status_code,'msg':'','data':json}

def post(url,params=None,header={}):
    res = requests.post(url,json=params,headers=header)
    json = res.json()
    if res.status_code == 200:
        return {'status':200,'msg':'','data':json}
    return {'status':res.status_code,'msg':'','data':json}

def delete(url,path,header={}):
    url = url+'/'+path
    res = requests.delete(url,headers=header)
    if res.status_code == 204:
        return {'status':200,'data':res.text}
    return {'status':res.status_code,'data':res.text}
    