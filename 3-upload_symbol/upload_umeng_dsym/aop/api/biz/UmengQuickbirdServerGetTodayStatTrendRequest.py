# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class UmengQuickbirdServerGetTodayStatTrendRequest(BaseApi):
    """获取今日小时粒度的实时统计数据

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.umeng.uapm&n=umeng.quickbird.server.getTodayStatTrend&v=1&cat=default

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.dataSourceId = None
        self.type = None
        self.appVersion = None

    def get_api_uri(self):
        return '1/com.umeng.uapm/umeng.quickbird.server.getTodayStatTrend'

    def get_required_params(self):
        return ['dataSourceId', 'type']

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
