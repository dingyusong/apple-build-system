#!/usr/bin/env python3
from distutils.core import setup
setup(
    name = 'apple_build_system',
    version = '1.0.0',
    py_modules = ['1-build_ipa.build_ipa','2-upload_ipa.upload_ipa_to_fir','3-upload_symbol.upload_umeng_dsym.upload_symb_to_umeng','3-upload_symbol.upload_umeng_dsym.aop.api.biz','3-upload_symbol.upload_umeng_dsym.aop.api.commom'],
    author = 'dys',
    author_email = 'dys90@qq.com',
    url = 'https://github.com/DingYusong/',
    description = 'build ipa scrpit',    
)