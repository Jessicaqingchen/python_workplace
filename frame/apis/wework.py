import requests

from frame.apis.base_api import BaseApi


class WeWork(BaseApi):
    def __init__(self, corpid, corpsecret):
        super().__init__()
        self.access_token = self.get_token(corpid, corpsecret)

    def get_token(self, corpid, corpsecret):
        '''
        获取token
        :return: access_token
        '''
        url = ""
        params = {
            "corpid": self.corpid,
            "corpsecret": self.corpsecret
        }
        # 发起接口请求
        req = requests.get("GET", url=url, params=params)
        # 获取token
        token = req.json().get("access_token")
        return token