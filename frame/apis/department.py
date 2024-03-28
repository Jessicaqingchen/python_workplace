import os

import requests

from frame.apis.wework import WeWork
from testing.Utils import Utils


class Department(WeWork):
    '''
    接口实现只描述接口信息，不做断言等
    '''
    def __init__(self):
        path = os.sep.join([Utils.get_frame_root_path(), "config/secrets.yaml"])
        yaml_data = Utils.get_yaml_data(path)
        self.corpid = yaml_data.get("corpid").get("yinian")
        self.secret = yaml_data.get("secret").get("contact")

    def creat(self, data):
        '''
        创建部门
        :return:
        '''
        creat_url = ""
        params = {
            "access_token": self.access_token
        }
        # request封装后发起请求
        req = {
            "method": "POST",
            "url": creat_url,
            "params": params,
            "json": data
        }
        res = self.send_api(req)
        # req = requests.request("POST", url=creat_url,params=params, json=data)
        return res

    def update(self, data):
        '''
        更新部门
        :return:
        '''
        update_url = ""
        params = {
            "access_token": self.access_token
        }
        # request封装后发起请求
        req = {
            "method": "POST",
            "url": update_url,
            "params": params,
            "json": data
        }
        res = self.send_api(req)
        # req = requests.request("POST", url=update_url, params=params, json=data)
        return res
    def delete(self, _id):
        '''
        删除部门
        :return:
        '''
        delete_url = ""
        params = {
            "access_token": self.access_token,
            "id": _id
        }
        req = {
            "method": "POST",
            "url": delete_url,
            "params": params
        }
        res = self.send_api(req)
        # req = requests.request("POST", url=delete_url, params=params)
        return res

    def get(self, _id=None):
        '''
        查询部门
        :return:
        '''
        get_list_url = ""
        params = {
            "access_token": self.access_token,
            "id": _id
        }
        # request封装后发起请求
        req = {
            "method": "POST",
            "url": get_list_url,
            "params": params
        }
        res = self.send_api(req)
        # req = requests.request("GET", url=get_list_url, params=params)
        return res