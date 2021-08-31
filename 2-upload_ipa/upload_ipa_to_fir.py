#!/usr/bin/env python3
import os

class UploadIPAToFir:
    def __init__(self, * , path_ipa, fir_token, fir_shortlink, fir_logpath='', next=''):
        if fir_logpath:
            self.fir_logpath = fir_logpath
        else:
            dir = os.path.dirname(path_ipa)
            self.fir_logpath =  os.path.join(dir,'fir.log')

        print(self.fir_logpath)

        self.path_ipa = path_ipa    
        self.fir_token = fir_token
        self.fir_shortlink = fir_shortlink
        self.next = next

    def exec(self):        
        print("-----------apple-build-system: run upload ipa to fir start-----------")

        cmd = 'upload_to_fir'

        cmd += ' '
        cmd += self.path_ipa

        cmd += ' '
        cmd += self.fir_token

        cmd += ' '
        cmd += self.fir_shortlink
        
        cmd += ' '
        cmd += self.fir_logpath
        
        print(cmd)
        os.system(cmd)

        print("-----------apple-build-system: run upload ipa to fir done-----------")
        if self.next:
            self.next.exec()