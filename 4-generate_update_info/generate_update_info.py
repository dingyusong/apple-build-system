# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os

class GenerateUpdateInfo:
    def __init__(self, *, buildNo,updateMsg,updateInfo_path,url_to_download,next=''):
        self.buildNo                = buildNo
        self.updateMsg              = updateMsg
        self.updateInfo_path        = updateInfo_path
        self.url_to_download        = url_to_download                
        self.next                   = next

    def exec(self):
        print("-----------apple-build-system: run generate_update_info start-----------")        

        currentDir=os.path.dirname(os.path.abspath(__file__))
        templtePath=os.path.join(currentDir,'updateInfoTemplte')

        update_templte = open(templtePath, 'r').read()

        update_content = update_templte.replace("$BUILDID", self.buildNo)
        update_content = update_content.replace("$UPDATEMESSAGE", self.updateMsg)
        update_content = update_content.replace("$UPDATEURL", self.url_to_download)

        open(self.updateInfo_path, 'w').write(update_content)        

        print("-----------apple-build-system: run generate_update_info done-----------")        
        if self.next:
            self.next.exec()            
