#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'

import sys,os,json
from common import connectool
from connectapi import ConnectApi
import click

@click.group()
def cli():
    '''
    app store connect api cli with python
    
    user apikey and issuer_id to authorize
    
    how to get apikey and issuer_id ?
    
    https://developer.apple.com/documentation/appstoreconnectapi
    
    '''

@click.command()
@click.option('-k','--apikey','apikey',metavar='',help='app store connect api key',required=True)
@click.option('-i','--issuer','issuer_id',metavar='',help='app store connect issuer id',required=True)
@click.option('-n','--name','name',metavar='',help='device name')
@click.option('-u','--udid','udid',metavar='',help='device udid')
def registerdevice(apikey,issuer_id,name,udid):
    '''register device into app store connect with name and udid '''
    result = ConnectApi(apikey,issuer_id).register_device(name,udid)
    click.echo(json.dumps(result))

@click.command()
@click.option('-k','--apikey','apikey',metavar='',help='app store connect api key',required=True)
@click.option('-i','--issuer','issuer_id',metavar='',help='app store connect issuer id',required=True)
@click.option('-l','--limit','limit',metavar='',help='the devices count,default 100')
@click.option('-s','--sort','sort',metavar='',help='the devices sort,default id')
def devices(apikey,issuer_id,limit,sort):
    '''list devices with limit and sort '''
    result = ConnectApi(apikey,issuer_id).list_devices(limit,sort)
    click.echo(json.dumps(result))

cli.add_command(registerdevice)
cli.add_command(devices)

if __name__ == '__main__':
    cli()
    # api = ConnectApi('T5VR6D3TZY','5127e6a3-99ef-458f-9ea3-ba6b76e9cc13')
    # api = ConnectApi('RVA59D6BQ9','2ab0a8e1-2389-4831-aac3-9abcad0ffedc')
    # api = ConnectApi('2D8S9X3462','ee792585-a5d8-4140-97e5-c356cd8112a8')
    
    # devices = api.list_devices(limit=1)
    # print(devices)
    
    # result = api.register_device('test','test')
    # print(result)
    
    
    
    
    # result = api.register_certificate(csr_path='/Users/last/Desktop/CertificateSigningRequest.certSigningRequest')
    # print(result)
    
    # result = api.delete_certificate('N9P79WJTHK')
    # print(result)
    
    # result = api.list_certificates()
    # print(result)
    
    # result = api.register_bundle_id(bundle_id='com.hepburn.app',team_id='6DD349HLLU',name='hepburn')
    # print(result)
    
    # result = api.list_bundle_ids()
    # print(result)
    
    # result = api.get_bundle_id('N49MX9AWAX')
    # print(result)
    
    # result = api.get_bundle_id_profiles('N49MX9AWAX')
    # print(result)
    
    # result = api.delete_bundle_id('N49MX9AWAX')
    # print(result)
    
    # result = api.create_profile(name='adhoc1',bundle_id='VSLGJ82UHW',certificate_id='T553J666XW',type='IOS_APP_DEVELOPMENT')
    # print(result)
    
    # result = api.delete_profile('4KVXW4LK52')
    # print(result)
    
    # result = api.list_profiles()
    # print(result)
    
    # result = api.request_profile('4KVXW4LK52')
    # print(result)