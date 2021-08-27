# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import aop
import aop.api
import requests
import os

class UploadDSYMToUmeng:
    def __init__(self, *, appKey, apiKey, apiSecurity, pathToSym, appVersion, fileName, next=''):
        self.appKey         = appKey
        self.apiKey         = apiKey
        self.apiSecurity    = apiSecurity
        self.pathToSym      = pathToSym
        self.appVersion     = appVersion
        self.fileName       = fileName
        self.next           = next

    def exec(self):
        print("-----------apple-build-system: run upload symbol to umeng start-----------")
        # 设置网关域名
        aop.set_default_server('gateway.open.umeng.com')

        # 设置apiKey和apiSecurity
        aop.set_default_appinfo(self.apiKey, self.apiSecurity)

        # 构造Request和访问协议是否是https
        req = aop.api.UmengQuickbirdSymUploadRequest()

        # 发起Api请求
        try:
            resp = req.get_response(None, dataSourceId=self.appKey, appVersion=self.appVersion, fileType=3, fileName=self.fileName)
            print('get upload parameters success!')
            self.postSymbolFile(resp)     
            # self.uploadWithBash(resp)       
        except aop.ApiError as e:
            # Api网关返回的异常
            print("ApiError:" + e)
        except aop.AopError as e:
            # 客户端Api网关请求前的异常
            print('AopError: '+ e)
        except Exception as e:
            # 其它未知异常
            print("Exception: " + e)
        print("-----------apple-build-system: run upload symbol to umeng done-----------")
        if self.next:            
            print('run next')
            self.next.exec()            


    def postSymbolFile(self, resp):
        data = {'OSSAccessKeyId':resp['accessKeyId'],
                'key'           :resp['key'],
                'policy'        :resp['policy'],
                'signature'     :resp['signature'],
                'callback'      :resp['callback'],
                }
        files={'file': open(self.pathToSym, 'rb')}
        r = requests.post(
                url=resp['uploadAddress'],
                data=data,
                files=files)        
        if(r.status_code == 200):
            print('upload symbol success!')
        else:
            print('upload symbol failure!'+ str(r.status_code) + r.reason)

    def uploadWithBash(self, resp):        
        currentDir=os.path.dirname(os.path.abspath(__file__))
        script = os.path.join(currentDir,'upload_umeng.sh')

        cmd = 'sh ' + script
        print(cmd)

        cmd += ' '
        cmd += resp['uploadAddress']
        print(cmd)

        cmd += ' '
        cmd += resp['accessKeyId']
        print(cmd)

        cmd += ' '
        cmd += resp['key']
        print(cmd)

        cmd += ' '
        cmd += resp['policy']
        print(cmd)

        cmd += ' '
        cmd += resp['signature']
        print("-----signature-----")
        print(cmd)

        cmd += ' '
        cmd += resp['callback']
        print(cmd)

        cmd += ' '
        cmd += self.pathToSym

        print(cmd)
        os.system(cmd)
