# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class UmengQuickbirdSymUploadRequest(BaseApi):
    """通过该接口获取文件上传的地址、签名等必要参数，有效期30分钟

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.umeng.uapm&n=umeng.quickbird.sym.upload&v=1&cat=default

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.dataSourceId = None
        self.appVersion = None
        self.fileType = None
        self.fileName = None

    def get_api_uri(self):
        return '1/com.umeng.uapm/umeng.quickbird.sym.upload'

    def get_required_params(self):
        return ['dataSourceId', 'appVersion', 'fileType', 'fileName']

    def get_multipart_params(self):
        return []

    def need_sign(self):
        return True

    def need_timestamp(self):
        return False

    def need_auth(self):
        return False

    def is_inner_api(self):
        return False
