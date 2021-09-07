#!/usr/bin/env python3
import os

class UploadIPAToAppStore:
    def __init__(self, * , path_ipa, apiKey, apiIssuer, next=''):
        self.path_ipa = path_ipa    
        self.apiKey = apiKey
        self.apiIssuer = apiIssuer
        self.next = next

    def exec(self):        
        print("-----------apple-build-system: run upload ipa to appstore start-----------")

        cmd = 'upload_to_appstore'

        cmd += ' '
        cmd += self.apiKey

        cmd += ' '
        cmd += self.apiIssuer

        cmd += ' '
        cmd += self.path_ipa
        
        print(cmd)
        os.system(cmd)

        print("-----------apple-build-system: run upload ipa to appstore done-----------")
        if self.next:
            self.next.exec()