## 环境 Python 3.7 +

## virtualenv
安装
pip3 install virtualenv

1.创建一个独立的Python运行环境
virtualenv --no-site-packages venv

2.进入环境
source venv/bin/activate

3.退出环境
deactivate

4.编译
python setup.py install

5.运行
connectcli

### 第三方库
pip3 install authlib

pip3 install requests


### api 

```
    api = ConnectApi('T5VR6D3TZY','5127e6a3-99ef-458f-9ea3-ba6b76e9cc13')
    # api = ConnectApi('S6RCGRV7MB','2ab0a8e1-2389-4831-aac3-9abcad0ffedc')
    
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
```

####  查询udid接口

```
响应 array 
    [{
        "type":"devices",
        "id":"23MQNW864Z",
        "attributes":{
            "addedDate":"2019-08-16T06:13:47.000+0000",
            "name":"大可爱的iPhone",
            "deviceClass":"IPHONE",
            "model":"iPhone 6",
            "udid":"6517b4ed0db1f3523ac0b6675c706985f35119fb",
            "platform":"IOS",
            "status":"ENABLED"
        },
        "links":{
            "self":"https://api.appstoreconnect.apple.com/v1/devices/23MQNW864Z"
        }
    }]
```

#### 查询bundleid接口

```
响应 array 
    [{
            "type":"bundleIds",
            "id":"5FC33TN7DC",
            "attributes":{
                "name":"hepburn",
                "identifier":"com.hepburn.app",
                "platform":"IOS",
                "seedId":"6DD349HLLU"
            },
            "relationships":{
                "bundleIdCapabilities":{
                    "meta":{
                        "paging":{
                            "total":0,
                            "limit":2147483647
                        }
                    },
                    "links":{
                        "self":"https://api.appstoreconnect.apple.com/v1/bundleIds/5FC33TN7DC/relationships/bundleIdCapabilities",
                        "related":"https://api.appstoreconnect.apple.com/v1/bundleIds/5FC33TN7DC/bundleIdCapabilities"
                    }
                },
                "profiles":{
                    "meta":{
                        "paging":{
                            "total":0,
                            "limit":2147483647
                        }
                    },
                    "links":{
                        "self":"https://api.appstoreconnect.apple.com/v1/bundleIds/5FC33TN7DC/relationships/profiles",
                        "related":"https://api.appstoreconnect.apple.com/v1/bundleIds/5FC33TN7DC/profiles"
                    }
                }
            },
            "links":{
                "self":"https://api.appstoreconnect.apple.com/v1/bundleIds/5FC33TN7DC"
            }
        }]

```

```
# # 请求设备列表
    # result = ConnectManager().list_devices(ConnectApi.connect_api_devices.value[0],limit=1)
    # if result['status'] == 200:
    #     array = result['data']
    #     connectool.prints(json.dumps(array))
    # else:
    #     connectool.prints(result)
    
    #查找profile
    # result = connectManager.request_profile(ConnectApi.connect_api_profiles.value[0],id='')
    # if result['status'] == 200:
    #     array = result['data']
    #     connectool.prints(json.dumps(array))
    # else:
    #     connectool.prints(result)
    
    
    # #获取profiles
    # result = connectManager.list_profiles(ConnectApi.connect_api_profiles.value[0])
    # if result['status'] == 200:
    #     array = result['data']
    #     connectool.prints(json.dumps(array))
    # else:
    #     connectool.prints(result)
    
    # # 删除profile
    # result = connectManager.delete_profile(ConnectApi.connect_api_profiles.value[0],id='')
    # connectool.prints(result)
    
    # # 创建 profile 文件
    # result = connectManager.create_profile(ConnectApi.connect_api_profiles.value[0],name='adhoc',bundle_id='',cerificate_id='',devices='')
    # if result:
    #     connectool.prints(result)
    
    # # 删除证书
    # result = connectManager.delete_certificate(ConnectApi.connect_api_certificates.value[0],id='X3HL3NXHV8')
    # connectool.prints(result)
    
    # #获取证书
    # result = connectManager.list_certificates(ConnectApi.connect_api_certificates.value[0])
    # if result['status'] == 200:
    #     array = result['data']
    #     connectool.prints(json.dumps(array))
    # else:
    #     connectool.prints(result)
    
    #创建证书
    # result = connectManager.register_certificate(ConnectApi.connect_api_certificates.value[0],type='IOS_DEVELOPMENT',csr_path='/Users/last/Desktop/CertificateSigningRequest.certSigningRequest')
    # if result:
    #     connectool.prints(result)
    
    # #获取bundle id profiles
    # result = connectManager.get_bundle_id_profiles(ConnectApi.connect_api_bundle_ids.value[0],id='8JM2624295')
    # if result['status'] == 200:
    #     array = result['data']
    #     connectool.prints(json.dumps(array))
    # else:
    #     connectool.prints(result)
    
    # #获取bundle id 信息
    # result = connectManager.get_bundle_id(ConnectApi.connect_api_bundle_ids.value[0],id='8JM2624295')
    # if result['status'] == 200:
    #     array = result['data']
    #     connectool.prints(json.dumps(array))
    # else:
    #     connectool.prints(result)
    
    # # 删除bundle id
    # result = connectManager.delete_bundle_id(ConnectApi.connect_api_bundle_ids.value[0],id='TBZZB9W9TV')
    # connectool.prints(result)
    
    # # 请求bundle id列表
    # result = connectManager.list_bundle_ids(ConnectApi.connect_api_bundle_ids.value[0],limit=10)
    # if result['status'] == 200:
    #     array = result['data']
    #     connectool.prints(json.dumps(array))
    # else:
    #     connectool.prints(result)
    
    # #注册bundle id
    # result = connectManager.register_bundle_id(ConnectApi.connect_api_bundle_ids.value[0],bundle_id='com.hepburn.app',team_id='6DD349HLLU',name='hepburn')
    # if result['status'] == 201:
    #     res = result['data']
    #     connectool.prints(json.dumps(res))
    # else:
    #     connectool.prints(result)
    
    # #请求添加设备
    # result = connectManager.register_device(ConnectApi.connect_api_devices.value[0],name='test2',udid='85ED42D5BD2D7F24DA197616C0230A11C47849EF')
    # if result['status'] == 201:
    #     res = result['data']
    #     connectool.prints(json.dumps(res))
    # else:
    #     connectool.prints(result)
```