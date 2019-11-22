#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yuyuan yue'

import json
import base64
import click

#读json，path：json文件路径，返回json对象
def loadJson(path):
    with open(path,'r') as fp:
        try:
            return json.load(fp)
        except Exception as excep:
            click.echo (path)
            click.echo (excep)

#写json文件，data：json数据，path：写入的路径
def saveJson(data,path):
    jsonData = json.dumps(data,indent=4, ensure_ascii=False,sort_keys=True)
    fileObject = open(path,'w')
    fileObject.write(jsonData)
    fileObject.close()
    
def loadFile(path):
    with open(path,'r') as fp:
        try:
            return fp.read()
        except Exception as excep:
            click.echo (path)
            click.echo (excep)

def saveFile(data,path):
    with open(path,'w') as fp:
        try:
            return fp.write(data)
        except Exception as excep:
            click.echo (path)
            click.echo (excep)

def saveByteFile(data,path):
    with open(path,'wb') as fp:
        try:
            return fp.write(data)
        except Exception as excep:
            click.echo (path)
            click.echo (excep)
            
def base64decode(content):
    return base64.b64decode(content)

def prints(params):
    click.echo(params)
    click.echo('\n')
    
def raiseError(msg):
    raise Exception(msg)

