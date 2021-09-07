#!/usr/bin/env python3
import os
from datetime import datetime

class IPABuilder:
    def __init__(self, * , path_xp, platform='ios', path_ws='', build_no=0, scheme='', version='',export_option_method='development', bitcode_enable='true',next=''):
        if build_no == 0:
            build_no = datetime.now().strftime('%Y%m%d%H%M%S')
        self.platform = platform    
        self.path_xp = path_xp
        self.path_ws = path_ws
        self.build_no = build_no
        self.version = version
        self.bitcode_enable = bitcode_enable        
        self.export_option_method = export_option_method
        if scheme:
            self.scheme = scheme
        else:            
            self.scheme = os.path.basename(path_xp).split('.')[0]
        self.next = next

    def exec(self):
        print("-----------apple-build-system: run build ipa start-----------")        
        cmd = 'build_ipa'

        cmd += ' -x '
        cmd += self.path_xp
            
        cmd += ' -b '
        cmd += str(self.build_no)

        cmd += ' -e '
        cmd += self.export_option_method
        
        cmd += ' -c '
        cmd += self.bitcode_enable

        if self.path_ws:
            cmd += ' -w '
            cmd += self.path_ws

        if self.scheme:  
            cmd += ' -s '
            cmd += self.scheme              

        if self.version:  
            cmd += ' -v '
            cmd += self.version              

        print(cmd)
        os.system(cmd)
        print("-----------apple-build-system: run build ipa done-----------")        
        if self.next:
            self.next.exec()            

    def build_ipa_path(self):
        if self.platform == 'ios':
            return os.path.join(self.build_dir(),self.scheme+'.ipa')
        if self.platform == 'mac':
            return os.path.join(self.build_dir(),self.scheme+'.app')

    def build_dir(self):
        dir = os.path.dirname(self.path_xp)        
        return os.path.join(dir,'build',self.scheme,str(self.build_no))

    def build_symbol_path(self):
        return os.path.join(self.build_dir(),self.build_symbol_name())
    
    def build_symbol_name(self):
        return self.scheme+'.app.dSYM.zip'

    def build_ipa_version(self):
        return self.version