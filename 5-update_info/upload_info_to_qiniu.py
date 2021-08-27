# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os

class UploadInfoToQiNiu:
    def __init__(self, *, ak, sk, space, path_update_info = '', update_url, refershName,next=''):
        self.ak                     = ak
        self.sk                     = sk
        self.space                  = space
        if path_update_info:
            self.path_update_info       = path_update_info
        else:
            self

        self.update_url             = update_url
        self.refershName            = refershName
        
        self.next                   = next

    def exec(self):
        print("-----------apple-build-system: run upload_info_to_qiniu start-----------")        
        cmd = 'upload_info_to_qiniu'

        cmd += ' -a '
        cmd += self.ak
        
        cmd += ' -s '
        cmd += self.sk

        cmd += ' -p '
        cmd += self.space

        cmd += ' -i '
        cmd += self.path_update_info
        cmd += ' -u '
        cmd += self.update_url
        cmd += ' -n '
        cmd += self.refershName

        print(cmd)
        os.system(cmd)
        print("-----------apple-build-system: run upload_info_to_qiniu done-----------")        
        if self.next:
            self.next.exec()            
