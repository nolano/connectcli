
# connectcli

app store connect api 封装工具，使用密钥对鉴权，支持命令行

关于密钥生成，请查看[app store connect api](https://developer.apple.com/documentation/appstoreconnectapi)


## 上手指南

登陆app store connect 获取apikey，issuerid，private_key文件（linux，mac系统建议在本地用户根目录下建立.private_keys文件夹，将private_keys文件放入该文件夹中，工具检测没有private_key 参数时会去该目录查找）

安装connectcli

```
pip3 install connectcli
```

### 命令行


#### 帮助

```
connectcli --help

Usage: connectcli [OPTIONS] COMMAND [ARGS]...

  app store connect api cli with python user apikey private_key and
  issuer_id to authorize

  how to get apikey,private_key and issuer_id ?
  https://developer.apple.com/documentation/appstoreconnectapi

Options:
  -k, --apikey            app store connect api key  [required]
  -i, --issuer            app store connect issuer id  [required]
  -p, --privatekey_path   privatekey file path , default linux user root path
                          ".private_keys"
  --help                  Show this message and exit.

Commands:
  bundleids            list bundleids with limit and sort
  certificates         list certificate with limit and sort
  createprofile        create profile with...
  deletebundleid       delete bundleid with id
  deletecertificate    delete certificate with id
  deleteprofile        delete profile with id
  devices              list devices with limit and sort
  getbundleid          get bundleid with id
  getbundleidprofiles  get bundleid profiles with id
  profiles             list profiles with limit and sort
  registerbundleid     register bundle id into app store connect with...
  registercertificate  register certificate with csr_path,out_path and type
  registerdevice       register device into app store connect with name and...
  requestprofile       request profile with id

```

#### 示例

```
connectcli -k T5VR6D3TZY -i 5127e6a3-99ef-458f-9ea3-ba6b76e9cc13 devices

result:

https://api.appstoreconnect.apple.com/v1/devices

{'Authorization': 'Bearer eyJraWQiOiJUNVZSNkQzVFpZIiwidHlwIjoiSldUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiI1MTI3ZTZhMy05OWVmLTQ1OGYtOWVhMy1iYTZiNzZlOWNjMTMiLCJleHAiOjE1NzQ3NjAzNjUsImF1ZCI6ImFwcHN0b3JlY29ubmVjdC12MSJ9.a0q5LxRN76VEpQjIu3_TqCD45iqeaEmcsb7BRawrN_Fts85MpPDgEb9RpZkoh18Qb0Xu2i9jTHip_l1nQt8WJg'}

{'limit': 1, 'sort': 'id'}

{"status": 200, "data": [{"type": "devices", "id": "23MQNW864Z", "attributes": {"addedDate": "2019-08-16T06:13:47.000+0000", "name": "\u5927\u53ef\u7231\u7684iPhone", "deviceClass": "IPHONE", "model": "iPhone 6", "udid": "6517b4ed0db1f3523ac0b6675c706985f35119fb", "platform": "IOS", "status": "ENABLED"}, "links": {"self": "https://api.appstoreconnect.apple.com/v1/devices/23MQNW864Z"}}]}

```

### API
 
```
from connectcli import ConnectApi

if __name__ == '__main__':
    api = ConnectApi('T5VR6D3TZY','5127e6a3-99ef-458f-9ea3-ba6b76e9cc13')
    
    devices = api.list_devices(limit=1)
    print(devices)
    
    result = api.register_device('name','udid')
    print(result)
    
    result = api.register_certificate(csr_path='/Users/last/Desktop/CertificateSigningRequest.certSigningRequest')
    print(result)
    
    result = api.delete_certificate('N9P79WJTHK')
    print(result)
    
    result = api.list_certificates()
    print(result)
    
    result = api.register_bundle_id(bundle_id='com.hepburn.app',team_id='6DD349HLLU',name='hepburn')
    print(result)
    
    result = api.list_bundle_ids()
    print(result)
    
    result = api.get_bundle_id('N49MX9AWAX')
    print(result)
    
    result = api.get_bundle_id_profiles('N49MX9AWAX')
    print(result)
    
    result = api.delete_bundle_id('N49MX9AWAX')
    print(result)
    
    result = api.create_profile(name='adhoc1',bundle_id='VSLGJ82UHW',certificate_id='T553J666XW',type='IOS_APP_DEVELOPMENT')
    print(result)
    
    result = api.delete_profile('4KVXW4LK52')
    print(result)
    
    result = api.list_profiles()
    print(result)
    
    result = api.request_profile('4KVXW4LK52')
    print(result)

```
