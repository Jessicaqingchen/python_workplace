import requests


class BaseApi:
    def __init__(self):
        pass

    def send_api(self, **kwargs):
        '''
        对request进行二次封装
        :return:对应接口
        '''
        return requests.request(**kwargs)